import {
  CHANGED_TYPE_OF_BRIEF,
  COMPLETED_GOAL,
  FAILED_GOAL,
} from "../types.js";
import { removeServerError, addServerError } from "../topError.js";
import api from "../../api.js";
import { store } from "../../index.js";

/**
 * changeTypeOfBrief
 *
 * @param {String} briefType - 'appbrief' 'respbrief' 'replybrief'
 *
 * Make an api call to the backend after we change the inputs.
 * If we are successful, dispatch a few things:
 *  1. CHANGED_TYPE_OF_BRIEF - Actually change the text on the page.
 *  2. removeServerError - If we previously had server issues, remove the text at the top.
 *  3. checkIfCompletedGoal - Checks if we should cross out 'Type of Brief' on the checklist.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 */
export default (briefType) => (dispatch) => {
  const formData = createFormData(briefType);

  if (cancelTypeChange(briefType)) {
    return;
  }

  api
    .coverKey("type", formData)
    .then((res) => {
      const { coverPage } = res.data;

      dispatch({
        type: CHANGED_TYPE_OF_BRIEF,
        payload: coverPage,
      });

      removeServerError(dispatch);

      const { type } = coverPage;
      checkIfCompletedGoal(type, dispatch);
    })
    .catch((err) => {
      addServerError(err, dispatch);
    });
};

/**
 * createFormData
 *
 * @param {String} briefType - The type of brief ( appbrief, respbrief, replybrief )
 * @return {FormData}
 *
 * Just creating our form data with our string.
 */
function createFormData(briefType) {
  let formData = new FormData();
  formData.append("value", briefType);
  return formData;
}

/**
 * checkIfCompletedGoal
 *
 * @param {Object} defendant - New type object.
 * @param {Function} dispatch - Dispatch function for the reducers.
 *
 * Checks our newly typed object for the error
 */
function checkIfCompletedGoal(type, dispatch) {
  if (!type.error) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "typeInput",
    });
  } else {
    dispatch({
      type: FAILED_GOAL,
      payload: "typeInput",
    });
  }
}

/**
 * cancelTypeChange
 *
 * @param {String} briefType - 'appbrief' 'respbrief' 'replybrief'
 *
 * If we select the same type that we already have,
 * we just dont even make the api call.
 */
function cancelTypeChange(briefType) {
  const currentState = store.getState();
  const currentType = currentState.cover.type.text;
  return briefType === currentType;
}
