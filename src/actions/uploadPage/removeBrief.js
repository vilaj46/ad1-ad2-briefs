import { FAILED_GOAL, REMOVED_BRIEF, DEACTIVATED_FILE } from "../types.js";
import { removeTopError, addServerError } from "../topError.js";
import api from "../../api.js";
import { store } from "../../index.js";

/**
 * removeBrief
 *
 * Make an api call to the backend after we remove our uploaded brief.
 * If we are successful, dispatch a few things:
 *  1. dispatchFailedGoal - If we have to uncheck the Upload Brief file.
 *  2. SYNCED_DATA - Resets the necessary data.
 *  3. dispatchActivatedFie - If our brief is activated.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 */
export default () => (dispatch) => {
  api
    .reset()
    .then((res) => {
      const { brief, cover, toa, toc, uploads } = res.data;

      dispatchFailedGoal(dispatch);

      dispatch({
        type: REMOVED_BRIEF,
        payload: { brief, cover, toa, toc, uploads },
      });

      dispatchActivatedFile(dispatch);

      removeTopError(dispatch);
    })
    .catch((err) => {
      addServerError(err, dispatch);
    });
};

/**
 * dispatchFailedGoal
 *
 * @param {Function} dispatch - Dispatch for the reducers.
 *
 * Checks if our 'Upload Brief file' is crossed out. If it is crossed out
 * we have to uncheck it.
 */
function dispatchFailedGoal(dispatch) {
  const currentState = store.getState();
  const { completed } = currentState.checklist[0].checklist[0];
  if (completed) {
    dispatch({ type: FAILED_GOAL, payload: "uploadBrief" });
  }
}

/**
 * dispatchActivatedFile
 *
 * @param {Function} dispatch - Dispatch for the reducers.
 *
 * Our brief will be the activated file so we have to remove it.
 * We check just to make sure.
 */
function dispatchActivatedFile(dispatch) {
  const currentState = store.getState();
  const { file } = currentState.active;
  if (Object.keys(file).length > 0) {
    dispatch({
      type: DEACTIVATED_FILE,
    });
  } else {
    return;
  }
}
