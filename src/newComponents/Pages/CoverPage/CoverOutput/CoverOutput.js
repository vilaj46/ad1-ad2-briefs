import React from "react";
import { connect } from "react-redux";

import styles from "./CoverOutput.module.css";
import coverStyles from "../CoverPage.module.css";

const CoverOutput = ({ cover }) => {
  const { indexNumber, plaintiff, defendant, type } = cover;
  const output = `${indexNumber.formatted} ${plaintiff.text} v ${defendant.text}_${type.text}`;
  return (
    <div className={styles.coverOutput}>
      <div className={coverStyles.thickDivider} />
      <div className={coverStyles.thinDivider} />
      <p className={styles.output}>{output}</p>
      <div className={coverStyles.thinDivider} />
      <div className={coverStyles.thickDivider} />
    </div>
  );
};

const mapStateToProps = (state) => {
  const { cover } = state;
  if (Object.keys(cover).length > 0) {
    return {
      cover,
    };
  } else {
    return {
      cover: {
        indexNumber: {
          formatted: "",
        },
        plaintiff: "",
        defendant: "",
        type: "",
      },
    };
  }
};

export default connect(mapStateToProps)(CoverOutput);
