import { REMOVED_TOA_ENTRIES, FAILED_GOAL } from "../types.js";
import { removeServerError, addServerError } from "../topError.js";
import api from "../../api.js";
import { store } from "../../index.js";

/**
 * removeAllEntries
 *
 *
 * If we are successful, dispatch a few things:
 *  1. dispatchGoals - Sets the appropriate status on the checklist.
 *  2. removeServerError - If we previously had server issues, remove the text at the top.
 *  3. REMOVED_TOC_ENTRIES - Actually change the entries on the page and make sure tocEntries/NumbersError are appropriate.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 */
export default () => (dispatch) => {
  api
    .removeTOAEntries()
    .then((res) => {
      const { entries, toaEntriesError, toaNumbersError } = res.data;
      dispatchGoals(toaEntriesError, toaNumbersError, dispatch);

      dispatch({
        type: REMOVED_TOA_ENTRIES,
        payload: {
          entries,
          toaEntriesError,
          toaNumbersError,
        },
      });

      removeServerError(dispatch);
    })
    .catch((err) => {
      addServerError(err, dispatch);
    });
};

/**
 * dispatchGoals
 *
 * @param {Boolean} toaEntriesError - Status of text errors in the entries.
 * @param {Boolean} toaNumbersError - Status of page number errors in the entries.
 * @param {Function} dispatch - Function used to update the reducers.
 *
 * If statements used to reduce the amount of dispatches.
 */
function dispatchGoals(toaEntriesError, toaNumbersError, dispatch) {
  const currentState = store.getState();
  const { toa } = currentState;

  if (toaEntriesError !== toa.toaEntriesError && toaEntriesError === true) {
    dispatch({ type: FAILED_GOAL, payload: "entryTOATextHighlight" });
  }

  if (toaNumbersError !== toa.toaNumbersError && toaNumbersError === true) {
    dispatch({ type: FAILED_GOAL, payload: "entryTOANumberHighlight" });
  }
}
