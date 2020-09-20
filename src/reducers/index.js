import { combineReducers } from "redux";

import page from "./page.js";
import active from "./active.js";
import checklist from "./checklist.js";
import topError from "./topError.js";
import pdfs from "./pdfs.js";
import toc from "./toc.js";
import cover from "./cover.js";
import brief from "./brief.js";
import toa from "./toa.js";
import uploads from "./uploads.js";

export default combineReducers({
  page,
  active,
  checklist,
  topError,
  pdfs,
  toc,
  cover,
  brief,
  toa,
  uploads,
});
