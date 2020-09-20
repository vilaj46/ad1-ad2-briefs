import React from "react";

import coverStyles from "../CoverPage.module.css";
import styles from "./CoverHeader.module.css";

const CoverHeader = () => {
  return (
    <div className={styles.coverHeader}>
      <div className={`${coverStyles.thickDivider} ${styles.extraMargin}`} />
      <div className={coverStyles.thinDivider} />
      <p className={`${styles.supremeCourt} ${styles.headerText}`}>
        Supreme Court
      </p>
      <p className={`${styles.newYork} ${styles.headerText}`}>
        State of New York
      </p>
    </div>
  );
};
export default CoverHeader;
