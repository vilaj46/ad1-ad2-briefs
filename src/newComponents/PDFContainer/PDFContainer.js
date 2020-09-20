import React from "react";
import { connect } from "react-redux";

import styles from "./PDFContainer.module.css";

const PDFContainer = ({ activePage, pdfs }) => {
  let pdf = false;
  if (activePage === 1) {
    pdf = pdfs.cover;
  } else if (activePage === 2) {
    pdf = pdfs.toc;
  } else if (activePage === 3) {
    pdf = pdfs.toa;
  }

  if (pdf) {
    const blob = new Blob([pdf], { type: "application/pdf" });
    const objectURL = URL.createObjectURL(blob);
    return (
      <div className={styles.pdfContainer}>
        <iframe
          src={objectURL}
          title="Cover PDF"
          className={styles.pdf}
        ></iframe>
      </div>
    );
  } else {
    return <div></div>;
  }
};

const mapStateToProps = (state) => {
  const { page, brief, pdfs } = state;
  if (brief) {
    return {
      activePage: page.active,
      pdfs,
    };
  } else {
    return {
      activePage: page.active,
      pdfs: {},
    };
  }
};

export default connect(mapStateToProps)(PDFContainer);
