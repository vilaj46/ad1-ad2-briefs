import { LOADED_TOA, COMPLETED_GOAL, LOADED_TOA_PDF } from "../types.js";
import api from "../../api.js";
import { removeTopError, changeTopError, addServerError } from "../topError.js";

import { store } from "../../index.js";

/**
 * loadTOA
 *
 * # CHANGE THIS
 * Check whether or not we should even make the call. If it was loaded already or not.
 *
 * Make an api call to the backend if we change to the TOC page OR
 * if we are on the TOC page and we upload a brief.
 *
 * If we are successful and found the cover page, dispatch a few things:
 *  1. LOADED_TOC - Actually change the data on the page.
 *  2. removeTopError - If we previously had server issues or cover issues, remove the text at the top.
 *  3. dispatchGoals - Checks if we should cross out the items on the checklist or give them a red border.
 *
 * If we are unsuccessful, we are just going to display the new error at the top.
 */
export default () => (dispatch) => {
  if (allowLoadTOA()) {
    return api
      .toa()
      .then((res) => {
        const { toaPage } = res.data;
        dispatch({
          type: LOADED_TOA,
          payload: toaPage,
        });

        removeTopError(dispatch);

        dispatchGoals(dispatch, toaPage);
        return true;
      })
      .then(() => {
        // Was getting an error going to the TOAPage without cases uploaded.
        const currentState = store.getState();
        const { caseData } = currentState.uploads;
        if (caseData.length > 0) {
          api.toaPDF().then((res) => {
            dispatch({
              type: LOADED_TOA_PDF,
              payload: res.data,
            });
          });
        }
        return true;
      })
      .catch((err) => {
        const { toaPage } = err.response.data;
        dispatch({
          type: LOADED_TOA,
          payload: toaPage,
        });

        // I don't want message appearing on Review Page
        const activePage = store.getState().page.active;
        if (activePage !== 4) {
          if (err.response.status === 404) {
            dispatch(changeTopError("Table of Authorities page not found."));
          } else {
            addServerError(err, dispatch);
          }
        }
        return true;
      });
  }
};

/**
 * allowLoadTOC
 *
 * @return {Boolean} - Whether or not we want to make this api call.
 *
 * We check the currentState of our Table of Contents. If the Table of Contents
 * has already been loaded, we do not want make another call. This will give us issues on the backend
 * as well as make unnecessary calls from the front end.
 */
function allowLoadTOA() {
  const currentState = store.getState();
  const { toa } = currentState;
  if (Object.keys(toa).length > 0) {
    if (toa.loaded === true) {
      return false;
    } else {
      return true;
    }
  } else {
    return true;
  }
}

/**
 * dispatchGoals
 *
 * @param {Function} dispatch - Dispatch the data to our reducers.
 * @param {Object} tocPage - Newly obtained Table of Contents information.
 *
 * Checks what is complete and what isn't. Crosses out the
 * appropriate.
 */
function dispatchGoals(dispatch, toaPage) {
  const { toaEntriesError, toaNumbersError } = toaPage;
  if (toaEntriesError === false) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "entryTOATextHighlight",
    });
  }
  if (toaNumbersError === false) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "entryTOANumberHighlight",
    });
  }
}
