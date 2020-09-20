import React from "react";
import {
  COMPLETED_GOAL,
  FAILED_GOAL,
  CHANGED_PAGE,
  CHECK_CASES_FOR_COMPLETION,
  CHANGED_DEPARTMENT,
} from "../actions/types.js";

import styles from "../newComponents/LeftNavigation/Checklist/Checklist.module.css";

const INITIAL_STATE = [
  {
    text: "Upload",
    label: "U",
    checklist: [
      {
        element: (
          <p key="uploadBrief" className={styles.inherit}>
            Upload <span className={styles.remove}>a</span> brief{" "}
            <span className={styles.remove}>file</span>
          </p>
        ),
        completed: false,
        id: "uploadBrief",
      },
      {
        element: (
          <p key="uploadCases" className={styles.inherit}>
            Upload case<span className={styles.opposite}>s</span>{" "}
            <span className={styles.remove}>files</span>
          </p>
        ),
        completed: false,
        id: "uploadCases",
      },
    ],
  },
  {
    text: "Covers",
    label: "C",
    checklist: [
      {
        element: <p>Defendant</p>,
        completed: false,
        id: "defendantInput",
      },
      {
        element: <p>Plaintiff</p>,
        completed: false,
        id: "plaintiffInput",
      },
      {
        element: <p>Index Number</p>,
        completed: false,
        id: "indexNumberInput",
      },
      {
        element: <p>Type of Brief</p>,
        completed: false,
        id: "typeInput",
      },
      {
        element: <p>Department</p>,
        completed: false,
        id: "departmentInput",
      },
    ],
  },
  {
    text: "Table of Contents",
    label: "TC",
    checklist: [
      {
        element: <p>TOC Entries</p>,
        completed: false,
        id: "entryTOCTextHighlight",
      },
      {
        element: <p>TOC Page Numbers</p>,
        completed: false,
        id: "entryTOCNumberHighlight",
      },
    ],
  },
  {
    text: "Table of Authorities",
    label: "TA",
    checklist: [
      {
        element: <p>TOA Entries</p>,
        completed: false,
        id: "entryTOATextHighlight",
      },
      {
        element: <p>TOA Page Numbers</p>,
        completed: false,
        id: "entryTOANumberHighlight",
      },
    ],
  },
  {
    text: "Review",
    label: "R",
    checklist: [
      {
        element: <p>Visted Upload Page</p>,
        completed: true,
        id: "vistitedUploadPage",
      },
      {
        element: <p>Visted Cover Page</p>,
        completed: false,
        id: "vistitedCoverPage",
      },
      {
        element: <p>Visted Table of Contents Page</p>,
        completed: false,
        id: "vistitedTableOfContents",
      },
      {
        element: <p>Visted Table of Authorities Page</p>,
        completed: false,
        id: "vistitedTableOfAuthorities",
      },
    ],
  },
];

/**
 * changeStatusOfGoalToTrue
 *
 * @param {String} completedGoal - The of the action dispatched.
 * @param {Object} state - Current state.
 *
 * If we complete a goal, search for it and set to true.
 */
const changeStatusOfGoalToTrue = (completedGoal, state) => {
  for (let i = 0; i < state.length; i++) {
    for (let j = 0; j < state[i].checklist.length; j++) {
      if (completedGoal === state[i].checklist[j].id) {
        state[i].checklist[j].completed = true;
        return [...state];
      }
    }
  }
  return [...state];
};

/**
 * changeStatusOfGoalToFalse
 *
 * @param {String} completedGoal - The of the action dispatched.
 * @param {Object} state - Current state.
 *
 * If we complete a goal, search for it and set to false.
 */
const changeStatusOfGoalToFalse = (completedGoal, state) => {
  for (let i = 0; i < state.length; i++) {
    for (let j = 0; j < state[i].checklist.length; j++) {
      if (completedGoal === state[i].checklist[j].id) {
        state[i].checklist[j].completed = false;
        return [...state];
      }
    }
  }
  return [...state];
};

/**
 * setReviewAfterPageVisit
 *
 * @param {Object} state - Current state.
 * @param {Number} payload - Page we Visited
 *
 * If we visit a page, we want to check off visited a page on the ReviewPage.
 */
const setReviewAfterPageVisit = (state, payload) => {
  const isBriefUploaded = state[0].checklist[0].completed;
  if (isBriefUploaded && payload !== 4) {
    state[4].checklist[payload].completed = true;
    return state;
  } else {
    return state;
  }
};

/**
 * setCasesCompleted
 *
 * @param {Object} state - Current state.
 * @param {String} payload - Our current department.
 *
 * If our case is for the First Department, we don't need the cases.
 * Therefore, the Upload Cases should be complete.
 */
const setCasesCompleted = (state, payload) => {
  const areCasesCompleted = state[0].checklist[1].completed;
  if (areCasesCompleted === false && payload.text === "First") {
    state[0].checklist[1].completed = true;
  } else if (areCasesCompleted === true && payload.text === "First") {
    state[0].checklist[1].completed = true;
  }
  return state;
};

export default (state = INITIAL_STATE, action = {}) => {
  switch (action.type) {
    case COMPLETED_GOAL:
      const newStateTrue = changeStatusOfGoalToTrue(action.payload, state);
      return [...newStateTrue];
    case FAILED_GOAL:
      const newStateFalse = changeStatusOfGoalToFalse(action.payload, state);
      return [...newStateFalse];
    case CHANGED_PAGE:
      const newStateAfterPageVisit = setReviewAfterPageVisit(
        state,
        action.payload
      );
      return newStateAfterPageVisit;
    case CHECK_CASES_FOR_COMPLETION:
      const newStateAfterCheckingCases = setCasesCompleted(
        state,
        action.payload
      );
      return newStateAfterCheckingCases;
    case CHANGED_DEPARTMENT:
      const newStateAfterDepartmentChange = setCasesCompleted(
        state,
        action.payload.department
      );
      return newStateAfterDepartmentChange;
    default:
      return state;
  }
};
