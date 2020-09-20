import {
  COMPLETED_GOAL,
  FAILED_GOAL,
  DEACTIVATED_FILE,
  UPLOADED_BRIEF,
} from "../types.js";
import { removeTopError, addServerError } from "../topError.js";
import api from "../../api.js";
import { store } from "../../index.js";
import loadCover from "../coverPage/loadCover.js";
import loadTOC from "../tocPage/loadTOC.js";
import loadTOA from "../toaPage/loadTOA.js";

/**
 * uploadBrief
 *
 * Make an api call to the backend after we uploaded a brief.
 * If we are successful, dispatch a few things:
 *  1. UPLOADED_BRIEF - This will reset our brief data if there is any and update our list of files.
 *  2. checkIfCompletedGoal - Check if the brief has non ocred pages or is a duplicate.
 *  3. performUploadFromAnotherPage - If we use the LargeBriefForm to upload the brief, we
 *     still have to upload the data to that page. Pages send for the data when they are loaded.
 *  4. removeTopError - If we had a error at the top, remove it.
 *  5. closeSpotlight - If our currently activated file is a brief, remove it.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 *
 * Whether our upload was successful or not, we check if a brief file is in the Spotlight.
 * If it is, remove it from the Spotlight. If its just a case, keep it.
 */
export default (e) => (dispatch) => {
  if (allowedToUpload(e)) {
    const formData = createFormData(e);
    api
      .upload(formData)
      .then((res) => {
        const { brief, toc, uploads, cover, toa } = res.data;

        dispatch({
          type: UPLOADED_BRIEF,
          payload: {
            brief,
            toc,
            uploads,
            cover,
            toa,
          },
        });

        checkIfCompletedGoal(uploads, dispatch);

        performUploadFromAnotherPage(dispatch);

        removeTopError(dispatch);

        closeSpotlight(dispatch);
      })
      .catch((err) => {
        addServerError(err, dispatch);
      });
  }
};

/**
 * closeSpotlight
 *
 * @param {Function} dispatch - Dispatch function for the reducers.
 *
 * If we upload a new brief while having the current brief under
 * the spotlight, we close the spotlight.
 */
function closeSpotlight(dispatch) {
  const currentState = store.getState();
  const activeFile = currentState.active.file;
  if (activeFile.type === "brief") {
    dispatch({
      type: DEACTIVATED_FILE,
    });
  }
}

/**
 * allowedToUpload
 *
 * @param {Object} e - event object.
 * @return {Boolean} - return Boolean whether the check is good or not.
 * Checks whether we are allowed to upload a new file.
 * We make sure there is actually a file being uploaded. This prevents the escape key error.
 * We then make sure the path is not the same as our currently uploaded brief.
 */
function allowedToUpload(e) {
  const currentState = store.getState();
  const prevFilePath = currentState.brief.filePath;
  const { files } = e.target;
  const currFilePath = files.length > 0 ? e.target.files[0].path : "";

  if (prevFilePath !== currFilePath && currFilePath) {
    return true;
  } else {
    return false;
  }
}

/**
 * checkIfCompletedGoal
 *
 * @param {Object} uploadPage - Recently acquired information.
 * @param {Function} dispatch - Dispatch function for the reducers.
 *
 * We just want to check if the brief is fully ocred and
 * if it is a duplicate file.
 */
function checkIfCompletedGoal(uploads, dispatch) {
  const { badPages, duplicate } = uploads.briefFile;
  if (badPages.length === 0 && !duplicate) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "uploadBrief",
    });
  } else {
    dispatch({
      type: FAILED_GOAL,
      payload: "uploadCases",
    });
  }
}

/**
 * performUploadFromAnotherPage
 *
 * @param {Function} dispatch - Dispatch function for the reducers.
 *
 * Checks whether we are on the upload page or not.
 * If we are not on the upload page and our briefFile does not exist,
 * we now we are uploading from the LargeBriefForm. The necessary pages will not
 * perform the componentDidMount function because the page has already been loaded.
 * This function will perform the required to get our data for that page.
 */
function performUploadFromAnotherPage(dispatch) {
  const currentState = store.getState();
  const { active } = currentState.page;
  if (active === 1) {
    dispatch(loadCover());
  } else if (active === 2) {
    dispatch(loadTOC());
  } else if (active === 3) {
    dispatch(loadTOA());
  }
}

function createFormData(e) {
  const n = e.target.files[0].name;
  const p = e.target.files[0].path;
  let formData = new FormData();
  formData.append("name", n);
  formData.append("path", p);
  return formData;
}
