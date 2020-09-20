import React from "react";
import { connect } from "react-redux";

import styles from "./TopError.module.css";

const TopError = ({ topError }) => {
  return (
    <div className={styles.block}>
      <h2 className={styles.topError}>{topError || ""}</h2>
    </div>
  );
};

const mapStateToProps = (state) => {
  const { topError } = state;
  return {
    topError,
  };
};

export default connect(mapStateToProps)(TopError);
