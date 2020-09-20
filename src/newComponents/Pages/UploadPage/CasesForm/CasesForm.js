import React from "react";
import { connect } from "react-redux";

import styles from "./CasesForm.module.css";
import attachment from "../../../../svgs/attachment.svg";
import attachment_hover from "../../../../svgs/attachment_hover.svg";

import uploadCases from "../../../../actions/uploadPage/uploadCases.js";

class CasesForm extends React.Component {
  onMouseEnter = () => {
    const img = document.getElementById("cases-svg");
    img.setAttribute("src", attachment_hover);
  };

  onMouseLeave = () => {
    const img = document.getElementById("cases-svg");
    img.setAttribute("src", attachment);
  };

  render() {
    const { uploadCases } = this.props;
    return (
      <form className={styles.top}>
        <label
          id="uploadCases"
          className={styles.filelabel}
          onMouseEnter={this.onMouseEnter}
          onMouseLeave={this.onMouseLeave}
        >
          <img
            src={attachment}
            alt="Attachment"
            className={styles.attachment}
            id="cases-svg"
          />
          <span className={styles.title}>Add Cases</span>
          <input
            className={styles.FileInput}
            name="attachment"
            type="file"
            id="casesForm"
            multiple
            accept="application/pdf"
            onChange={uploadCases}
          />
        </label>
      </form>
    );
  }
}

export default connect(null, { uploadCases })(CasesForm);
