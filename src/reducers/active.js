import {
  ACTIVATED_FILE,
  CHANGED_PAGE,
  DEACTIVATED_FILE,
  UPLOADED_BRIEF,
  REMOVED_CASE,
  REMOVED_BRIEF,
} from "../actions/types.js";

const INITIAL_STATE = {
  file: {
    fileName: "",
    badPages: "",
    filePath: "",
    type: "",
    duplicate: false,
    IDNumber: -1,
  },
  toc: {},
  toa: {},
};

export default (state = INITIAL_STATE, action = {}) => {
  switch (action.type) {
    case ACTIVATED_FILE:
      // If its the same file, just close it.
      if (action.payload.IDNumber === state.file.IDNumber) {
        return { ...state, file: { ...INITIAL_STATE.file } };
      }
      return { ...state, file: action.payload };
    case DEACTIVATED_FILE: {
      return { ...state, file: { ...INITIAL_STATE.file } };
    }
    case CHANGED_PAGE:
      return { ...INITIAL_STATE };
    case UPLOADED_BRIEF:
      // If we upload a brief with the brief in the spotlight, close it.
      if (state.file.type === "brief") {
        return { ...state, file: { ...INITIAL_STATE.file } };
      } else {
        return { ...state };
      }
    case REMOVED_BRIEF:
      return { ...state, file: { ...INITIAL_STATE.file } };
    case REMOVED_CASE:
      if (state.file.type === "case") {
        return { ...state, file: { ...INITIAL_STATE.file } };
      } else {
        return { ...state };
      }
    default:
      return state;
  }
};
