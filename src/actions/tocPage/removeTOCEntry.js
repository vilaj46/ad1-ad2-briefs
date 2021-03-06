import { REMOVED_TOC_ENTRY, FAILED_GOAL, COMPLETED_GOAL } from "../types.js";
import { removeServerError, addServerError } from "../topError.js";
import api from "../../api.js";
import { store } from "../../index.js";

/**
 * removeTOCEntry
 *
 *
 * @param {String} IDNumber - The id of the entry we right clicked.
 *
 * If we are successful, dispatch a few things:
 *  1. dispatchGoals - Sets the appropriate status on the checklist.
 *  2. removeServerError - If we previously had server issues, remove the text at the top.
 *  3. REMOVED_TOC_ENTRY - Actually change the entries on the page and make sure tocEntries/NumbersError are appropriate.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 */
export default (IDNumber) => (dispatch) => {
  api
    .removeTOCEntry(IDNumber)
    .then((res) => {
      const { entries, tocEntriesError, tocNumbersError } = res.data;
      dispatchGoals(tocEntriesError, tocNumbersError, dispatch);
      dispatch({
        type: REMOVED_TOC_ENTRY,
        payload: {
          entries,
          tocEntriesError,
          tocNumbersError,
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
 * @param {Boolean} tocEntriesError - Status of text errors in the entries.
 * @param {Boolean} tocNumbersError - Status of page number errors in the entries.
 * @param {Function} dispatch - Function used to update the reducers.
 *
 * If statements used to reduce the amount of dispatches.
 */
function dispatchGoals(tocEntriesError, tocNumbersError, dispatch) {
  const currentState = store.getState();
  const { toc } = currentState;

  if (tocEntriesError !== toc.tocEntriesError && tocEntriesError === true) {
    dispatch({ type: FAILED_GOAL, payload: "entryTOCTextHighlight" });
  } else if (
    tocEntriesError !== toc.tocEntriesError &&
    tocEntriesError === false
  ) {
    dispatch({ type: COMPLETED_GOAL, payload: "entryTOCTextHighlight" });
  }

  if (tocNumbersError !== toc.tocNumbersError && tocNumbersError === true) {
    dispatch({ type: FAILED_GOAL, payload: "entryTOCNumberHighlight" });
  } else if (
    tocNumbersError !== toc.tocNumbersError &&
    tocNumbersError === false
  ) {
    dispatch({ type: COMPLETED_GOAL, payload: "entryTOCNumberHighlight" });
  }
}
