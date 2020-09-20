import React from "react";
import ReactDOM from "react-dom";
import { Provider } from "react-redux";
import thunk from "redux-thunk";
import { createStore, applyMiddleware } from "redux";
import rootReducer from "./reducers";

import App from "./newComponents/App/App";
import "./index.css";

export const store = createStore(rootReducer, applyMiddleware(thunk));

/**
 * Loading modals for everything?
 *
 * IndexNumberInput bugged when typing.
 *
 * Figure out how to get pagelabel from toc to blank., its coming up as toc, tod, etc...
 *
 * TOA page instead of iframe, have the option of both
 *
 * Remove first page of cases if it has the search page.
 *
 */

/**
 * Things we want:
 * If we click on the checklist, it should highlight and display extra steps or whats wrong if there is a problem.
 * Ability to just change the output name. Do we put this on the cover page or the review page?
 * Error messages for the inputs
 * Remove all entries option on the Tableof Contents and Table of Authorities
 * Checklist on the upload page should highlight the 'Add Cases' first then look for any errors in the cases and highlight them as well.
 * SHOW PAGES IN 'PDF' or 'BRIEF' ABOVE THE PAGE NUMBERS / offer an option to change them.
 * SERVER HELP / CONFIGURATION IF WE FAIL.
 *
 */

ReactDOM.render(
  <Provider store={store}>
    <App />
  </Provider>,
  document.getElementById("root")
);
