import { CHANGED_PAGE } from "./types.js";

/**
 * changePage
 *
 * @param {Number} page - What page we are to load.
 *
 * 0 - Upload Page
 * 1 - Cover Page
 * 2 - Table of Contents Page
 * 3 - Table of Authorities Page
 * 4 - Review Page
 *
 * Dispatch the CHANGED_PAGE action to change our page.
 */

export default (page) => (dispatch) => {
  dispatch({
    type: CHANGED_PAGE,
    payload: page,
  });
};
