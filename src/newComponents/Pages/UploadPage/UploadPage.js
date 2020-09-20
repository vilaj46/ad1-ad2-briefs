import React from "react";

import BriefForm from "./BriefForm/BriefForm";
import CasesForm from "./CasesForm/CasesForm";
import styles from "./UploadPage.module.css";

import FileEntries from "./FileEntries/FileEntries";

const UploadPage = () => (
  <div>
    <div className={styles.grid}>
      <BriefForm />
      <CasesForm />
    </div>
    <FileEntries />
  </div>
);

export default UploadPage;
