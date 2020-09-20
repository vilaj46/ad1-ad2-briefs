import { LOADED_TOC, COMPLETED_GOAL, LOADED_TOC_PDF } from "../types.js";
import api from "../../api.js";
import { removeTopError, changeTopError, addServerError } from "../topError.js";

import { store } from "../../index.js";

/**
 * loadTOC
 *
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
  if (allowLoadTOC()) {
    api
      .toc()
      .then((res) => {
        const { tocPage } = res.data;
        dispatch({
          type: LOADED_TOC,
          payload: tocPage,
        });

        removeTopError(dispatch);

        // dispatch goals here once we figure it out.
        dispatchGoals(dispatch, tocPage);
      })
      .then(() => {
        api.tocPDF().then((res) => {
          dispatch({
            type: LOADED_TOC_PDF,
            payload: res.data,
          });
        });
      })
      .catch((err) => {
        const { tocPage } = err.response.data;
        dispatch({
          type: LOADED_TOC,
          payload: tocPage,
        });

        // I don't want message appearing on Review Page
        const activePage = store.getState().page.active;
        if (activePage !== 4) {
          if (err.response.status === 404) {
            dispatch(changeTopError("Table of Contents page not found."));
          } else {
            addServerError(err, dispatch);
          }
        }
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
function allowLoadTOC() {
  const currentState = store.getState();
  const { toc } = currentState;

  if (Object.keys(toc).length > 0) {
    if (toc.loaded === true) {
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
function dispatchGoals(dispatch, tocPage) {
  const { tocEntriesError, tocNumbersError } = tocPage;

  if (tocEntriesError === false) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "entryTOCTextHighlight",
    });
  }
  if (tocNumbersError === false) {
    dispatch({
      type: COMPLETED_GOAL,
      payload: "entryTOCNumberHighlight",
    });
  }
}
