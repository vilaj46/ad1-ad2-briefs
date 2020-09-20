import {
  SYNCED_DATA,
  UPLOADED_BRIEF,
  REMOVED_BRIEF,
  CREATED_OUTPUT_FILE,
} from "../actions/types.js";

const INITIAL_STATE = {};

export default (state = INITIAL_STATE, action = {}) => {
  switch (action.type) {
    case SYNCED_DATA:
      return { ...action.payload.brief };
    case UPLOADED_BRIEF:
      return { ...action.payload.brief };
    case REMOVED_BRIEF:
      return { ...action.payload.brief };
    case CREATED_OUTPUT_FILE:
      return { ...state, outputPath: action.payload };
    default:
      return state;
  }
};
