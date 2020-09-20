import {
  FAILED_GOAL,
  DEACTIVATED_FILE,
  COMPLETED_GOAL,
  UPLOADED_CASE,
  UNLOADED_TOA,
} from "../types.js";
import { removeTopError, addServerError } from "../topError.js";
import api from "../../api.js";
import { store } from "../../index.js";

/**
 * uploadCases
 *
 * Make an api call to the backend after we uploaded case(s)s.
 * First we check if we are actually uploading files. This prevents an error when we just close the
 * directory.
 * If we are successful, dispatch a few things:
 *  1. UPLOADED_CASE - This will reset our cases data if there is any and update our list of files.
 *  2. checkIfCompletedGoal - Checks the caseFilesError which was already done in the backend.
 *  3. removeTopError - If we had a error at the top, remove it.
 *  4. closeSpotlight - Check if we need to close the spotlight.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 *
 * Whether our upload was successful or not, we check if a case file is in the Spotlight.
 * If it is, remove it from the Spotlight. If its just a brief, keep it.
 */
export default (e) => (dispatch) => {
  const { files } = e.target;
  if (files.length > 0) {
    const formData = createFormData(files);
    api
      .cases(formData)
      .then((res) => {
        const { uploads } = res.data;

        dispatch({
          type: UPLOADED_CASE,
          payload: uploads,
        });

        const { caseFilesError } = uploads;
        checkIfCompletedGoal(caseFilesError, dispatch);

        removeTopError(dispatch);

        closeSpotlight(dispatch);

        setLoadedToFalse(dispatch);
      })
      .catch((err) => {
        addServerError(err, dispatch);
      });
  }
};

/**
 * setLoadedToFalse
 *
 * @param {Function} dispatch - Function to produce the actions.
 *
 * If we forget to upload cases initially and load our TOA page, it will not reload
 * after we upload cases.
 */
function setLoadedToFalse(dispatch) {
  const currentState = store.getState();
  const { loaded } = currentState.toa;
  if (loaded) {
    dispatch({
      type: UNLOADED_TOA,
    });
  }
}

/**
 * createFormData
 *
 * @param {Array} files - The uploaded files from our 'mulitple' input.
 * @return {FormData} - Newly created Form Data with our file paths.
 *
 * Iterate over our files grabbing the necessary file path.
 */
function createFormData(files) {
  let formData = new FormData();
  Array.from(files).forEach((f, i) => {
    formData.append(f.path, "");
  });
  return formData;
}

/**
 * checkIfCompletedGoal
 *
 * @param {Boolean} caseFilesError - Whether or not we contain an error
 * @param {Function} dispatch - Dispatch function for the reducers.
 *
 * The error has already been configured in the backend. With our
 * new upload page, we get the most current status (caseFilesError).
 */
export function checkIfCompletedGoal(caseFilesError, dispatch) {
  if (caseFilesError === true) {
    dispatch({
      type: FAILED_GOAL,
      payload: "uploadCases",
    });
  } else {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "uploadCases",
    });
  }
}

/**
 * closeSpotlight
 *
 * @param {Function} dispatch - Dispatch function for the reducers.
 *
 * If we upload a new cases while having a case under
 * the spotlight, we close the spotlight.
 */
function closeSpotlight(dispatch) {
  const currentState = store.getState();
  const activeFile = currentState.active.file;
  if (activeFile.type === "case") {
    dispatch({
      type: DEACTIVATED_FILE,
    });
  }
}
