import api from "../../api.js";
import { removeTopError, addServerError } from "../topError.js";
import { CREATED_OUTPUT_FILE } from "../types.js";

/**
 * After clicking create output file on the Review Page,
 * we create the final final and display the output path on the review page.
 */
export default () => (dispatch) => {
  api
    .review()
    .then((res) => {
      const { outputPath } = res.data;

      dispatch({
        type: CREATED_OUTPUT_FILE,
        payload: outputPath,
      });

      removeTopError(dispatch);
    })
    .catch((err) => {
      addServerError(err, dispatch);
    });
};
