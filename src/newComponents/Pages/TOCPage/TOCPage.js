import React from "react";
import { connect } from "react-redux";

import styles from "./TOCPage.module.css";
import loadTOC from "../../../actions/tocPage/loadTOC";
import LargeBriefForm from "../UploadPage/BriefForm/LargeBriefForm";
import TOCEntries from "./TOCEntries/TOCEntries";

class TOCPage extends React.Component {
  componentDidMount = () => {
    const { brief, loadTOC } = this.props;
    if (brief.filePath.length > 0) {
      loadTOC();
    }
  };

  render() {
    const { brief, openTOCMenu, closeTOCMenu, showMenu } = this.props;
    return brief.filePath.length === 0 ? (
      <LargeBriefForm />
    ) : (
      <div className={styles.grid} onClick={this.onClick}>
        <p className={styles.headerText}>Table of Contents</p>
        <TOCEntries
          showMenu={showMenu}
          displayMenu={openTOCMenu}
          closeMenu={closeTOCMenu}
        />
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  const { brief } = state;
  if (brief && Object.keys(brief).length > 0) {
    return {
      brief,
    };
  } else {
    return {
      brief: { filePath: "" },
    };
  }
};

export default connect(mapStateToProps, { loadTOC })(TOCPage);
