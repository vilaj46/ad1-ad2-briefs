import { REMOVED_CASE, LOADED_TOA_PDF } from "../types.js";
import { removeTopError, addServerError } from "../topError.js";
import api from "../../api.js";
import { checkIfCompletedGoal } from "./uploadCases.js";
import { store } from "../../index.js";

/**
 * removeCase
 *
 * Make an api call to the backend after we remove an uploaded case.
 * If we are successful, dispatch a few things:
 *  1. REMOVED_CASE - This will reset our case data and our display of files.
 *  2. checkIfCompletedGoal - Will uncheck the 'Upload Cases' on the checklist if any of our files have an error.
 *  3. removeTopError - If we had a error at the top, remove it.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 */
export default (id) => (dispatch) => {
  api
    .removeCase(id)
    .then((res) => {
      const { uploads } = res.data;
      const { caseFilesError } = uploads;
      dispatch({
        type: REMOVED_CASE,
        payload: uploads,
      });

      checkIfCompletedGoal(caseFilesError, dispatch);

      removeTopError(dispatch);
    })
    .then(() => {
      // Was getting an error going to the TOAPage without cases uploaded.
      const currentState = store.getState();
      const { caseFiles } = currentState.uploads;
      const { pdfs } = currentState;
      if (caseFiles.length > 0 && pdfs.toa !== false) {
        api.toaPDF().then((res) => {
          dispatch({
            type: LOADED_TOA_PDF,
            payload: res.data,
          });
        });
      } else if (caseFiles.length === 0 && pdfs.toa) {
        dispatch({
          type: LOADED_TOA_PDF,
          payload: false,
        });
      }
    })
    .catch((err) => {
      addServerError(err, dispatch);
    });
};
