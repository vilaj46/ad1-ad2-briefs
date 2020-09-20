import React from "react";
import { connect } from "react-redux";

import styles from "./ReviewPage.module.css";
import changePage from "../../../actions/changePage.js";

const PageList = ({ checks, page, changePage }) => {
  let pageText = "";
  let column = "";
  let row = "";
  let id = "";

  switch (page) {
    case 0:
      pageText = "Upload Page";
      column = "3 / 5";
      row = "3 / 5";
      id = "vistitedUploadPage";
      break;
    case 1:
      pageText = "Cover Page";
      column = "6 / 8";
      row = "3 / 5";
      id = "vistitedCoverPage";
      break;
    case 2:
      pageText = "TOC Page";
      column = "3 / 5";
      row = "6 / 8";
      id = "vistitedTableOfContents";
      break;
    case 3:
      pageText = "TOA Page";
      column = "6 / 8";
      row = "6 / 8";
      id = "vistitedTableOfAuthorities";
      break;
    default:
      break;
  }

  return (
    <div
      className={styles.position}
      style={{ gridColumn: column, gridRow: row }}
    >
      <h3
        className={styles.listHeader}
        onClick={() => changePage(page)}
        id={id}
      >
        {pageText}
      </h3>
      <ul className={styles.checks}>
        {checks.checklist.map((check) => {
          return (
            <li
              style={{
                textDecoration: `${
                  check.id === "uploadBrief" ? "line-through" : ""
                }`,
              }}
              className={check.completed ? styles.completed : ""}
              key={check.id}
            >
              {check.element}
            </li>
          );
        })}
      </ul>
    </div>
  );
};

const mapStateToProps = (state) => {
  const { checklist } = state;
  return {
    checklist,
  };
};

export default connect(mapStateToProps, { changePage })(PageList);
