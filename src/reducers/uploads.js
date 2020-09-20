import {
  SYNCED_DATA,
  UPLOADED_CASE,
  UPLOADED_BRIEF,
  REMOVED_CASE,
  REMOVED_BRIEF,
} from "../actions/types.js";

const INITIAL_STATE = {};

export default (state = INITIAL_STATE, action = {}) => {
  switch (action.type) {
    case SYNCED_DATA:
      return { ...action.payload.uploads };
    case UPLOADED_BRIEF:
      return { ...action.payload.uploads };
    case UPLOADED_CASE:
      return { ...action.payload };
    case REMOVED_CASE:
      return { ...action.payload };
    case REMOVED_BRIEF:
      return { ...action.payload.uploads };
    default:
      return state;
  }
};
