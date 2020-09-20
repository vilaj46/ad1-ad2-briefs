import {
  LOADED_TOC,
  RESET_TOC,
  REMOVED_TOC_ENTRY,
  INSERTED_TOC_ENTRY,
  CHANGED_TOC_ENTRY,
  REMOVED_TOC_ENTRIES,
  SYNCED_DATA,
  UPLOADED_BRIEF,
  REMOVED_BRIEF,
} from "../actions/types.js";

const INITIAL_STATE = {};

export default (state = INITIAL_STATE, action = {}) => {
  switch (action.type) {
    case SYNCED_DATA:
      return { ...action.payload.uploads };
    case UPLOADED_BRIEF:
      return { ...action.payload.uploads };
    case LOADED_TOC:
      return { ...action.payload };
    case RESET_TOC:
      return { ...action.payload };
    case REMOVED_TOC_ENTRY:
      return {
        ...state,
        entries: action.payload.entries,
        tocEntriesError: action.payload.tocEntriesError,
        tocNumbersError: action.payload.tocNumbersError,
      };
    case REMOVED_TOC_ENTRIES:
      return {
        ...state,
        entries: action.payload.entries,
        tocEntriesError: action.payload.tocEntriesError,
        tocNumbersError: action.payload.tocNumbersError,
      };
    case INSERTED_TOC_ENTRY:
      return {
        ...state,
        entries: action.payload,
        tocEntriesError: true,
        tocNumbersError: true,
      };
    case CHANGED_TOC_ENTRY:
      return {
        ...state,
        entries: action.payload.entries,
        tocEntriesError: action.payload.tocEntriesError,
        tocNumbersError: action.payload.tocNumbersError,
      };
    case REMOVED_BRIEF:
      return {
        ...action.payload.toc,
      };
    default:
      return state;
  }
};
