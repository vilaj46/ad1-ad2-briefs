import React from "react";
import { connect } from "react-redux";

import styles from "./BriefForm.module.css";
import attachment from "../../../../svgs/attachment.svg";
import attachment_hover from "../../../../svgs/attachment_hover.svg";

import uploadBrief from "../../../../actions/uploadPage/uploadBrief.js";

class LargeBriefForm extends React.Component {
  onMouseEnter = () => {
    const img = document.getElementById("brief-svg");
    // Sometimes, the paperclip does not light up.
    img.setAttribute("src", attachment_hover);
  };

  onMouseLeave = () => {
    const img = document.getElementById("brief-svg");
    img.setAttribute("src", attachment);
  };

  render() {
    const { uploadBrief } = this.props;
    return (
      <form className={styles.largeBrief}>
        <label
          id="uploadBrief"
          className={styles.largeBriefLabel}
          onMouseEnter={this.onMouseEnter}
          onMouseLeave={this.onMouseLeave}
        >
          <img
            src={attachment}
            alt="Attachment"
            className={styles.attachment}
            id="brief-svg"
          />
          <span className={styles.title}>Add the Brief first!</span>
          <input
            className={styles.FileInput}
            name="attachment"
            type="file"
            id="briefForm"
            accept="application/pdf"
            onChange={uploadBrief}
          />
        </label>
      </form>
    );
  }
}

export default connect(null, { uploadBrief })(LargeBriefForm);
