import { SYNCED_DATA } from "../types.js";
import { removeTopError, addServerError } from "../topError.js";
import api from "../../api.js";

/**
 * syncFile
 *
 * @return {Boolean} This will enable or disable our application clicks.
 *
 * Make an api call to the backend after we start our application.
 * If we are successful, dispatch a few things:
 *  1. SYNCED_DATA - Resets the toc reducer.
 *  2. removeTopError - If we previously had server issues, remove the text at the top.
 *
 *  Once the app loads, we want to make sure all our data is reset from the previous brief.
 *  This will set the loaded state in our main App component. The loaded state either
 *  disables or enables our application.
 *
 * TODO:
 *  When our app fails to sync, we should offer options to fix it.
 */
export default () => async (dispatch) => {
  return api
    .sync()
    .then((res) => {
      const { brief, toc, toa, cover, uploads } = res.data;

      dispatch({
        type: SYNCED_DATA,
        payload: {
          toc,
          brief,
          toa,
          cover,
          uploads,
        },
      });

      removeTopError(dispatch);
      return true;
    })
    .catch((err) => {
      addServerError(err, dispatch);
      return false;
    });
};
