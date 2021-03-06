import { CHANGED_TOC_ENTRY, COMPLETED_GOAL, FAILED_GOAL } from "../types.js";
import api from "../../api.js";
import { removeServerError, addServerError } from "../topError.js";
import { store } from "../../index.js";

/**
 * changeEntry
 *
 * @param {Object} e - Not an actual event object because it was not being passed through the timeout.
 *
 * Make an api call to the backend after we change the inputs with a 1s delay.
 * If we are successful, dispatch a few things:
 *  1. dispatchGoals - Checks if we should cross out 'Entries' or 'Page Numbers' on the checklist.
 *  2. CHANGED_TOC_ENTRY - Actually change the entries on the page.
 *  3. removeServerError - If we previously had server issues, remove the text at the top.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 *
 * Special Note: dispatchGoals is first so we can compare the current checklist state
 * in order to reduce the reducer calls.
 */
export default (e, IDNumber) => (dispatch) => {
  const formData = createFormData(e, IDNumber);
  api
    .tocChangeEntry(IDNumber, formData)
    .then((res) => {
      const { entries, tocNumbersError, tocEntriesError } = res.data;

      dispatchGoals(dispatch, tocNumbersError, tocEntriesError);

      dispatch({
        type: CHANGED_TOC_ENTRY,
        payload: {
          entries,
          tocNumbersError,
          tocEntriesError,
        },
      });

      removeServerError(dispatch);
    })
    .catch((err) => {
      addServerError(err, dispatch);
    });
};

/**
 * createFormData
 *
 * @param {Object} e - Not the actual event object. Contains the name and value.
 * @param {*} IDNumber - Our way of finding the entry we changed.
 * @return {FormData} - FormData object with our key, value, IDNumber.
 *
 * Creates our form data.
 */
function createFormData(e, IDNumber) {
  const { name, value } = e;
  let formData = new FormData();
  formData.append("key", name);
  formData.append("value", value);
  formData.append("IDNumber", IDNumber);
  return formData;
}

/**
 * dispatchGoals
 *
 * @param {Function} dispatch - Our function to reach the reducers.
 * @param {Boolean} currentTocNumbersError  - Whether or not the numbers of the entries have any issues.
 * @param {Boolean} currentTocEntriesError - Whether or not the text of the entries have any issues.
 *
 * Simply decides whether we are going to check off our boxes or not.
 * The if statements are used to reduce the reducer calls.
 */
function dispatchGoals(
  dispatch,
  currentTocNumbersError,
  currentTocEntriesError
) {
  const currentState = store.getState();
  const { tocNumbersError, tocEntriesError } = currentState.toc; // previous state

  // If we don't currently have an error AND we previously had an error.
  if (currentTocEntriesError === false && tocEntriesError) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "entryTOCTextHighlight",
    });
  } else if (currentTocEntriesError === true && tocEntriesError === false) {
    dispatch({
      type: FAILED_GOAL,
      payload: "entryTOCTextHighlight",
    });
  }

  if (currentTocNumbersError === false && tocNumbersError) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "entryTOCNumberHighlight",
    });
  } else if (currentTocNumbersError === true && tocNumbersError === false) {
    dispatch({
      type: FAILED_GOAL,
      payload: "entryTOCNumberHighlight",
    });
  }
}
