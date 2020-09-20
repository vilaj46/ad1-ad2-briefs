import { CHANGED_INDEX_NUMBER, COMPLETED_GOAL, FAILED_GOAL } from "../types.js";
import { removeServerError, addServerError } from "../topError.js";
import api from "../../api.js";

/**
 * changeIndexNumber
 *
 * @param {Object} e - Event of the inputs.
 *
 * Make an api call to the backend after we change the inputs.
 * If we are successful, dispatch a few things:
 *  1. CHANGED_INDEX_NUMBER - Actually change the text on the page.
 *  2. removeServerError - If we previously had server issues, remove the text at the top.
 *  3. checkIfCompletedGoal - Checks if we should cross out 'Index Number' on the checklist.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 */
export default (e) => (dispatch) => {
  const formData = createFormData(e);
  api
    .coverKey("indexNumber", formData)
    .then((res) => {
      const { coverPage } = res.data;
      dispatch({
        type: CHANGED_INDEX_NUMBER,
        payload: coverPage,
      });

      removeServerError(dispatch);

      const { indexNumber } = coverPage;
      checkIfCompletedGoal(indexNumber, dispatch);
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
 * The name is our key (number, year) and the value is our value.
 */
function createFormData(e) {
  let formData = new FormData();
  formData.append("value", [e.target.name, e.target.value]);
  return formData;
}

/**
 * checkIfCompletedGoal
 *
 * @param {Object} indexNumber - Recently acquired information.
 * @param {Function} dispatch - Dispatch function for the reducers.
 *
 * If either the indexNumber number or indexNumber year have
 * an error, we did not complete our goal.
 */
function checkIfCompletedGoal(indexNumber, dispatch) {
  if (!!indexNumber.indexError && !!indexNumber.yearError) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "indexNumberInput",
    });
  } else {
    dispatch({
      type: FAILED_GOAL,
      payload: "indexNumberInput",
    });
  }
}
