import { CHANGED_PAGE } from "../actions/types.js";

const INITIAL_STATE = {
  active: 0,
  visited: createNewSet(),
};

export default (state = INITIAL_STATE, action = {}) => {
  switch (action.type) {
    case CHANGED_PAGE:
      let newState = setNewState(state, action.payload);
      return newState;
    default:
      return state;
  }
};

/**
 * setNewState
 *
 * @param {Object} state - Current state.
 * @param {Number} payload - The page number we are on.
 *
 * Helper function to clean up the switch statement.
 */
function setNewState(state, payload) {
  return {
    ...state,
    active: payload,
    visited: state.visited.add(payload),
  };
}

/**
 * createNewSet
 *
 * Track the visited pages for the ReviewPage.
 * Use a set and default it with 0 because of the UploadPage.
 * This way our set ( could have been array ) does not keep adding pages.
 */
function createNewSet() {
  let set = new Set();
  set.add(0);
  return set;
}
