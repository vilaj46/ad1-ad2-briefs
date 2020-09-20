import {
  LOADED_COVER,
  CHANGED_DEPARTMENT,
  CHANGED_INDEX_NUMBER,
  CHANGED_TYPE_OF_BRIEF,
  CHANGED_PARTY,
  SYNCED_DATA,
  UPLOADED_BRIEF,
  REMOVED_BRIEF,
} from "../actions/types.js";

const INITIAL_STATE = {};

export default (state = INITIAL_STATE, action = {}) => {
  switch (action.type) {
    case SYNCED_DATA:
      return { ...action.payload.cover };
    case UPLOADED_BRIEF:
      return { ...action.payload.cover };
    case REMOVED_BRIEF:
      return { ...action.payload.cover };
    case LOADED_COVER:
      return { ...action.payload };
    case CHANGED_DEPARTMENT:
      return { ...action.payload };
    case CHANGED_INDEX_NUMBER:
      return { ...action.payload };
    case CHANGED_TYPE_OF_BRIEF:
      return { ...action.payload };
    case CHANGED_PARTY:
      return { ...action.payload };
    default:
      return state;
  }
};
