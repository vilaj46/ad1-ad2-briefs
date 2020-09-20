import React from "react";
import { connect } from "react-redux";

import styles from "./FileEntry.module.css";
import collapse from "../../../../images/collapse.png";
import docu from "../../../../images/document.png";
import gavel from "../../../../svgs/gavel.svg";

import { activateFile } from "../../../../actions/active.js";

const FileName = ({ data, activateFile, activeFileId }) => {
  const { badPages, duplicate, IDNumber, type, fileName } = data;
  const error =
    badPages.length > 0 || duplicate === true ? styles.entryError : "";
  const collapseRotate =
    activeFileId === IDNumber ? styles.collapse90 : styles.collapse;
  const imageSRC = type === "brief" ? docu : gavel;
  const title = type === "brief" ? "Brief" : "Decision";
  return (
    <div className={`${styles.entry} ${error}`}>
      <div
        className={styles.fileImageContainer}
        onClick={() => activateFile(data)}
      >
        <img
          src={collapse}
          alt="Collapse"
          className={`${styles.image} ${collapseRotate}`}
          title="Show more"
        />
      </div>
      <div className={styles.fileImageContainer}>
        <img
          src={imageSRC}
          alt="File"
          className={`${styles.image} ${styles.folder}`}
          title={title}
        />
      </div>
      <p className={`${styles.fileText} ${styles.bold}`}>{fileName}</p>
    </div>
  );
};

const mapStateToProps = (state) => {
  const { file } = state.active;
  return {
    activeFileId: file.IDNumber,
  };
};

export default connect(mapStateToProps, { activateFile })(FileName);
