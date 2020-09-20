import loadCover from "../coverPage/loadCover.js";
import loadTOA from "../toaPage/loadTOA.js";
import loadTOC from "../tocPage/loadTOC.js";

/**
 * If we do not visit any of the tabs except the Upload Page and the Review Page,
 * we will have the option to get all the information of the other pages before
 * continuing.
 */
export default () => async (dispatch) => {
  await dispatch(loadCover());
  await dispatch(loadTOA());
  await dispatch(loadTOC());
};
