import React from "react";
import { connect } from "react-redux";

import styles from "./ActiveStepLabel.module.css";

const ActiveStepLabel = ({ page, checklist }) => {
  return <h2 className={styles.main}>{checklist[page].text}</h2>;
};

const mapStateToProps = (state) => {
  const { page, checklist } = state;
  return { page: page.active, checklist };
};

export default connect(mapStateToProps)(ActiveStepLabel);
