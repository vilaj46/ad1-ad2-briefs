import { CHANGED_TOP_ERROR } from "./types.js";
import { store } from "../index.js";

/**
 * changeTopError
 *
 * @param {String} err - Message we want to display.
 *
 * Main function for changing the overhead message.
 */
export const changeTopError = (err) => {
  return {
    type: CHANGED_TOP_ERROR,
    payload: err,
  };
};

/**
 * removeTopError
 *
 * @param {Function} dispatch
 *
 * If we have a successful api call and we currently
 * have a top error, remove the top error. This also reduces the action dispatching.
 */
export const removeTopError = (dispatch) => {
  const currentState = store.getState();
  const { topError } = currentState;

  if (topError !== "") {
    dispatch(changeTopError(""));
  }
};

/**
 * removeServerError
 *
 * @param {Function} dispatch
 *
 * Checks if we are currently displaying the server error
 * and removes it. If we have another error we don't remove it.
 */
export const removeServerError = (dispatch) => {
  const currentState = store.getState();
  const { topError } = currentState;

  if (topError.includes("server")) {
    dispatch(changeTopError(""));
  }
};

/**
 * addServerError
 *
 * @param {Object} err - Our error object from api call.
 * @param {Function} dispatch
 *
 * Checks our error response from the api call.
 * If it is server related, we add the message to the top.
 * Otherwise, we just say something went wrong.
 */
export const addServerError = (err, dispatch) => {
  if (`${err}`.includes("Network")) {
    dispatch(changeTopError("Could not connect to server."));
  } else {
    dispatch(changeTopError("Something went wrong."));
  }
};
