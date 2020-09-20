import React from "react";

import styles from "./LNContainer.module.css";

import PageTabs from "../PageTabs/PageTabs";
import ActiveStepLabel from "../ActiveStepLabel/ActiveStepLabel";
import Checklist from "../Checklist/Checklist";

const LNContainer = () => {
  return (
    <aside className={styles.main}>
      <PageTabs />
      <div className={styles.sub}>
        <ActiveStepLabel />
        <Checklist />
      </div>
    </aside>
  );
};

export default LNContainer;
