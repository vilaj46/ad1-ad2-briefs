import React from "react";
import { connect } from "react-redux";

import appStyles from "../../../App/App.module.css";
import styles from "./BriefForm.module.css";
import attachment from "../../../../svgs/attachment.svg";
import attachment_hover from "../../../../svgs/attachment_hover.svg";

import uploadBrief from "../../../../actions/uploadPage/uploadBrief.js";

class BriefForm extends React.Component {
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
    const { brief, uploadBrief } = this.props;
    const toHighlightBriefForm =
      brief.fileName.length === 0 ? appStyles.highlightBorder : "";
    return (
      <form className={styles.top}>
        <label
          id="uploadBrief"
          className={`${styles.filelabel} ${toHighlightBriefForm}`}
          onMouseEnter={this.onMouseEnter}
          onMouseLeave={this.onMouseLeave}
        >
          <img
            src={attachment}
            alt="Attachment"
            className={styles.attachment}
            id="brief-svg"
          />
          <span className={styles.title}>Add Brief</span>
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
const mapStateToProps = (state) => {
  // Our initial load returns a blank object.
  const { brief } = state;

  if (brief && Object.keys(brief).length > 0) {
    return {
      brief,
    };
  } else {
    return {
      brief: {
        fileName: "",
      },
    };
  }
};

export default connect(mapStateToProps, { uploadBrief })(BriefForm);
