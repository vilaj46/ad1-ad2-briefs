import {
  LOADED_COVER,
  COMPLETED_GOAL,
  LOADED_COVERS_PDF,
  CHECK_CASES_FOR_COMPLETION,
} from "../types.js";
import api from "../../api.js";
import { removeTopError, changeTopError, addServerError } from "../topError.js";
import { store } from "../../index.js";

/**
 * loadCover
 *
 * Make an api call to the backend if we change to the cover page OR
 * if we are on the cover page and we upload a brief.
 *
 * If we are successful and found the cover page, dispatch a few things:
 *  1. LOADED_COVER - Actually change the data on the page.
 *  2. removeTopError - If we previously had server issues or cover issues, remove the text at the top.
 *  3. dispatchGoals - Checks if we should cross out the items on the checklist or give them a red border.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 */
export default () => (dispatch) => {
  api
    .covers()
    .then((res) => {
      const { coverPage } = res.data;

      if (typeof coverPage === "string") {
        throw coverPage;
      }

      dispatch({
        type: LOADED_COVER,
        payload: coverPage,
      });

      removeTopError(dispatch);

      dispatchGoals(dispatch, coverPage);

      dispatch({
        type: CHECK_CASES_FOR_COMPLETION,
        payload: coverPage.department,
      });
    })
    .then(() => {
      api.coverPDF().then((res) => {
        dispatch({
          type: LOADED_COVERS_PDF,
          payload: res.data,
        });
      });
    })
    .catch((err) => {
      const { coverPage } = err.response.data;
      dispatch({
        type: LOADED_COVER,
        payload: coverPage,
      });

      // I don't want message appearing on Review Page
      const activePage = store.getState().page.active;
      if (activePage !== 4) {
        if (err.response.status === 404) {
          dispatch(changeTopError("Cover page not found."));
        } else {
          addServerError(err, dispatch);
        }
      }
    });
};

/**
 * dispatchGoals
 *
 * @param {Function} dispatch - Dispatch the data to our reducers.
 * @param {Object} coverPage - Newly obtained cover information.
 *
 * Checks what is complete and what isn't. Crosses out the
 * appropriate.
 */
function dispatchGoals(dispatch, coverPage) {
  const { defendant, department, indexNumber, plaintiff, type } = coverPage;
  if (!defendant.error) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "defendantInput",
    });
  }
  if (!plaintiff.error) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "plaintiffInput",
    });
  }
  if (!department.error) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "departmentInput",
    });
  }
  if (!indexNumber.indexError && !indexNumber.yearError) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "indexNumberInput",
    });
  }
  if (!type.error) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "typeInput",
    });
  }
}
