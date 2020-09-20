import { CHANGED_PARTY, COMPLETED_GOAL, FAILED_GOAL } from "../types.js";
import { removeServerError, addServerError } from "../topError.js";
import api from "../../api.js";

/**
 * changeParty
 *
 * @param {Object} e - Event of the inputs.
 *
 * Make an api call to the backend after we change the inputs.
 * If we are successful, dispatch a few things:
 *  1. CHANGED_PARTY - Actually change the text on the page.
 *  2. removeServerError - If we previously had server issues, remove the text at the top.
 *  3. checkIfCompletedGoal - Checks if we should cross out 'Defendant' or 'Plaintiff' on the checklist.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 */
export default (e) => (dispatch) => {
  const formData = createFormData(e);

  api
    .coverKey(e.target.name, formData)
    .then((res) => {
      const { coverPage } = res.data;

      dispatch({
        type: CHANGED_PARTY,
        payload: coverPage,
      });

      removeServerError(dispatch);

      const { defendant, plaintiff } = coverPage;
      checkIfCompletedGoal(defendant, plaintiff, dispatch);
    })
    .catch((err) => {
      addServerError(err, dispatch);
    });
};

/**
 * createFormData
 *
 * @param {e} dept - Event with our name and value
 * @return {FormData}
 *
 * Just creating our form data with our event object.
 */
function createFormData(e) {
  let formData = new FormData();
  formData.append("value", e.target.value);
  return formData;
}

/**
 * checkIfCompletedGoal
 *
 * @param {String} defendant - New defendant object.
 * @param {String} plaintiff - New plaintiff object.
 * @param {Function} dispatch - Dispatch function for the reducers.
 *
 * Checks both and sets the appropriate state.
 */
function checkIfCompletedGoal(defendant, plaintiff, dispatch) {
  if (!defendant.error) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "defendantInput",
    });
  } else {
    dispatch({
      type: FAILED_GOAL,
      payload: "defendantInput",
    });
  }

  if (!plaintiff.error) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "plaintiffInput",
    });
  } else {
    dispatch({
      type: FAILED_GOAL,
      payload: "plaintiffInput",
    });
  }
}
