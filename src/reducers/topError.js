import { CHANGED_TOP_ERROR } from "../actions/types.js";

const INITIAL_STATE = "";

export default (state = INITIAL_STATE, action = {}) => {
  switch (action.type) {
    case CHANGED_TOP_ERROR:
      return action.payload;
    default:
      return state;
  }
};
