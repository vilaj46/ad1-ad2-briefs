import { CHANGED_DEPARTMENT, COMPLETED_GOAL } from "../types.js";
import { addServerError, removeServerError } from "../topError.js";
import api from "../../api.js";
import { store } from "../../index.js";

/**
 * changeDepartment
 *
 * @param {String} dept - Department we are changing to.
 *
 * First we check if we should make the change.
 * If we are allowed to, make an api call to the backend.
 * If we are successful, dispatch a few things:
 *  1. CHANGED_DEPARTMENT - Actually change the text on the page.
 *  2. removeServerError - If we previously had server issues, remove the text at the top.
 *  3. checkIfCompletedGoal - Checks if we should cross out 'Department' on the checklist.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 */
export default (dept) => (dispatch) => {
  const formData = createFormData(dept);

  if (cancelDepartmentChange(dept)) {
    return;
  }

  api
    .coverKey("department", formData)
    .then((res) => {
      const { coverPage } = res.data;

      dispatch({
        type: CHANGED_DEPARTMENT,
        payload: coverPage,
      });

      removeServerError(dispatch);

      const { department } = coverPage;
      checkIfCompletedGoal(department, dispatch);
    })
    .catch((err) => {
      addServerError(err, dispatch);
    });
};

/**
 * createFormData
 *
 * @param {String} dept - Department string
 * @return {FormData}
 * Just creating our form data with our department and setting it to value.
 */
function createFormData(dept) {
  let formData = new FormData();
  formData.append("value", dept);
  return formData;
}

/**
 * cancelDepartmentChange
 *
 * @param {String} dept - Department string
 *
 * If we select the same department that we already have,
 * we just dont even make the api call.
 */
function cancelDepartmentChange(dept) {
  const currentState = store.getState();
  const currentDepartment = currentState.cover.department.text;
  return dept === currentDepartment;
}

/**
 * checkIfCompletedGoal
 *
 * @param {String} department - Recently acquired information.
 * @param {Function} dispatch - Dispatch function for the reducers.
 *
 * We just check our new department information for the error.
 * At the moment, this could never be false because our only options
 * right now will complete the goal.
 */
function checkIfCompletedGoal(department, dispatch) {
  if (!department.error) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "departmentInput",
    });
  }
}
