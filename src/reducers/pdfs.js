import {
  LOADED_COVERS_PDF,
  LOADED_TOC_PDF,
  LOADED_TOA_PDF,
  UPLOADED_BRIEF,
  REMOVED_BRIEF,
} from "../actions/types.js";

const INITIAL_STATE = {
  cover: false,
  toc: false,
  toa: false,
};

export default (state = INITIAL_STATE, action = {}) => {
  switch (action.type) {
    case LOADED_COVERS_PDF:
      return { ...state, cover: action.payload };
    case LOADED_TOC_PDF:
      return { ...state, toc: action.payload };
    case LOADED_TOA_PDF:
      return { ...state, toa: action.payload };
    case REMOVED_BRIEF:
      return { ...INITIAL_STATE };
    case UPLOADED_BRIEF:
      return { ...INITIAL_STATE };
    default:
      return state;
  }
};
