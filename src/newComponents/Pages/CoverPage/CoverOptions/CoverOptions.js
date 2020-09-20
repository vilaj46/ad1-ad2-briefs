import React from "react";
import { connect } from "react-redux";

import styles from "./CoverOptions.module.css";

const CoverOptions = ({
  numCoverPages,
  pageNumberStartInPdf,
  pageNumberEndInPdf,
}) => {
  return (
    <ol className={styles.options}>
      <li>1. We found {numCoverPages || 0} cover page(s).</li>
      {numCoverPages !== false && numCoverPages !== 0 && (
        <li>2. Your cover starts on page {pageNumberStartInPdf}.</li>
      )}
      {numCoverPages !== false && numCoverPages !== 0 && (
        <li>3. Your cover ends on page {pageNumberEndInPdf}.</li>
      )}
    </ol>
  );
};

const mapStateToProps = (state) => {
  try {
    const {
      numCoverPages,
      pageNumberStartInPdf,
      pageNumberEndInPdf,
    } = state.cover;
    return {
      numCoverPages,
      pageNumberStartInPdf,
      pageNumberEndInPdf,
    };
  } catch {
    return {
      numCoverPages: 0,
      pageNumberStartInPdf: false,
      pageNumberEndInPdf: false,
    };
  }
};

export default connect(mapStateToProps)(CoverOptions);
