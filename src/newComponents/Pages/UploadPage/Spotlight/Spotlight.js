import React from "react";
import { connect } from "react-redux";

import styles from "./Spotlight.module.css";
import removeBrief from "../../../../actions/uploadPage/removeBrief.js";
import removeCase from "../../../../actions/uploadPage/removeCase.js";

const Spotlight = ({ file, removeBrief, removeCase, brief }) => {
  const onClick = () => {
    if (file.type === "brief") {
      removeBrief();
      const input = document.getElementById("briefForm");
      input.value = "";
    } else {
      removeCase(file.IDNumber);
      const input = document.getElementById("casesForm");
      input.value = "";
    }
  };

  const { fileName, filePath, badPages, duplicate, index } = file;

  // setup for our spotlight depending on the position of the file name we clicked.
  const spotlight = document.querySelector(`.${styles.main}`);
  if (spotlight) {
    const pos = calculatePosition(index, brief, {
      badPages,
      duplicate,
      fileName,
    });
    spotlight.setAttribute("style", `grid-column: 2; grid-row: ${pos}`);
  }

  return (
    Object.keys(file).length > 0 && (
      <div
        className={`${styles.main} ${filePath.length === 0 ? styles.hide : ""}`}
      >
        <button type="button" className={styles.button} onClick={onClick}>
          Remove
        </button>
        <p className={styles.text}>{fileName}</p>
        <p className={styles.text}>{filePath}</p>
        {badPages.length > 0 && (
          <p className={`${styles.text} ${styles.error}`}>
            Pages needing ocr: {badPages}
          </p>
        )}
        {duplicate === true && (
          <p className={`${styles.fileText} ${styles.error}`}>
            This is a duplicate file.
          </p>
        )}
      </div>
    )
  );
};

/**
 * calculatePosition
 *
 * @param {Number} index - Index tells us if we are using a brief or a case file.
 * @param {Object} brief - brief file information
 * @param {Object} fileData - selected file data
 * @return {String} Position in our grid
 *
 * We are given our index, the brief does not have an index. So if our index is
 * undefined we know its the brief and can just do row 1.  We then calculate how many
 * extra rows we need to fit the data in.
 *
 * If we do have an index, its a case. If we also have a brief upload, we need to
 * take that into account by giving our row a + 1. We then calculate the extra rows
 * based off our data.
 */
function calculatePosition(index, brief, fileData) {
  const { badPages, duplicate, fileName } = fileData;
  if (index === undefined) {
    const firstNumber = 1;
    const secondNumber =
      4 + Number(badPages.length > 0 ? 1 : 0) + Number(duplicate ? 1 : 0);
    return `${firstNumber} / ${secondNumber}`;
  } else {
    const { filePath } = brief;
    const newIndex = filePath.length > 0 ? index + 1 : index;
    const newBadPages = badPages.length > 0 ? 1 : 0;
    const newDuplicate = duplicate === true ? 1 : 0;
    const fnLength = Math.round(fileName.length / 50);
    return `${newIndex} / ${
      newIndex + newBadPages + newDuplicate + fnLength + 3
    }`;
  }
}

const mapStateToProps = (state) => {
  const { file } = state.active;
  const { brief } = state;
  return {
    file,
    brief,
  };
};

export default connect(mapStateToProps, { removeBrief, removeCase })(Spotlight);
