import {
  LOADED_TOA,
  UNLOADED_TOA,
  CHANGED_TOA_ENTRY,
  INSERTED_TOA_ENTRY,
  REMOVED_TOA_ENTRY,
  REMOVED_TOA_ENTRIES,
  SYNCED_DATA,
  UPLOADED_BRIEF,
  REMOVED_BRIEF,
  REMOVED_CASE,
} from "../actions/types.js";

const INITIAL_STATE = {};

export default (state = INITIAL_STATE, action = {}) => {
  switch (action.type) {
    case SYNCED_DATA:
      return { ...action.payload.toa };
    case UPLOADED_BRIEF:
      return { ...action.payload.toa };
    case LOADED_TOA:
      return { ...action.payload };
    case UNLOADED_TOA:
      return { ...state, loaded: false };
    case CHANGED_TOA_ENTRY:
      return {
        ...state,
        entries: action.payload.entries,
        toaEntriesError: action.payload.toaEntriesError,
        toaNumbersError: action.payload.toaNumbersError,
      };
    case INSERTED_TOA_ENTRY:
      return {
        ...state,
        entries: action.payload,
        toaEntriesError: true,
        toaNumbersError: true,
      };
    case REMOVED_TOA_ENTRY:
      return {
        ...state,
        entries: action.payload.entries,
        toaEntriesError: action.payload.toaEntriesError,
        toaNumbersError: action.payload.toaNumbersError,
      };
    case REMOVED_TOA_ENTRIES:
      return {
        ...state,
        entries: action.payload.entries,
        toaEntriesError: action.payload.toaEntriesError,
        toaNumbersError: action.payload.toaNumbersError,
      };
    case REMOVED_BRIEF:
      return {
        ...action.payload.toc,
      };
    case REMOVED_CASE:
      return { ...state, loaded: false };
    default:
      return state;
  }
};
