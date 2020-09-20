import { INSERTED_TOC_ENTRY, FAILED_GOAL } from "../types.js";
import { removeServerError, addServerError } from "../topError.js";
import api from "../../api.js";
import { store } from "../../index.js";

/**
 * insertTOCEntry
 *
 *
 * @param {String} IDNumber - The id of the entry we right clicked.
 * @param {Number} direction - -1 for inserting below, 1 for inserting above, 0 for changing the entry.
 *
 * If we are successful, dispatch a few things:
 *  1. failGoals - Removes the line through on our goals.
 *  2. INSERTED_TOC_ENTRY - Actually change the entries on the page and make sure tocEntries/NumbersError are true.
 *  3. removeServerError - If we previously had server issues, remove the text at the top.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 */

export default (IDNumber, direction) => (dispatch) => {
  api
    .insertTOCEntry(IDNumber, direction)
    .then((res) => {
      const { entries } = res.data;

      failGoals(dispatch);

      dispatch({
        type: INSERTED_TOC_ENTRY,
        payload: entries,
      });

      removeServerError(dispatch);
    })
    .catch((err) => {
      addServerError(err, dispatch);
    });
};

/**
 * failGoals
 *
 * @param {Function} dispatch - Function used to update our reducer.
 *
 * Checks whether there is a line through or not. If there is, we remove it.
 */
function failGoals(dispatch) {
  const currentState = store.getState();
  const { tocEntriesError, tocNumbersError } = currentState.toc;

  if (tocEntriesError === false) {
    dispatch({
      type: FAILED_GOAL,
      payload: "entryTOCTextHighlight",
    });
  }

  if (tocNumbersError === false) {
    dispatch({
      type: FAILED_GOAL,
      payload: "entryTOCNumberHighlight",
    });
  }
}
