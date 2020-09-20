import React from "react";
import { connect } from "react-redux";

import LargeBriefForm from "../UploadPage/BriefForm/LargeBriefForm";

import styles from "./TOAPage.module.css";

import loadTOA from "../../../actions/toaPage/loadTOA.js";
import TOAEntries from "./TOAEntries/TOAEntries";

class TOAPage extends React.Component {
  state = {
    loaded: false,
  };

  componentDidMount = () => {
    const { brief, loadTOA } = this.props;
    if (brief.filePath.length > 0) {
      try {
        loadTOA().then(() => {
          this.setState({ loaded: true });
        });
      } catch {
        this.setState({ loaded: true });
        return;
      }
    } else {
      this.setState({ loaded: true });
    }
  };

  // Not sure why I have this.
  // componentWillUnmount = () => {
  //   this.setState({ loaded: false });
  // };

  render() {
    const { brief, openTOAMenu, closeTOAMenu, showMenu } = this.props;
    const { loaded } = this.state;
    return brief.filePath.length === 0 ? (
      <LargeBriefForm />
    ) : (
      loaded && brief.filePath.length > 0 && (
        <div className={styles.grid} onClick={this.onClick}>
          <p className={styles.headerText}>Table of Authorities</p>
          <TOAEntries
            showMenu={showMenu}
            displayMenu={openTOAMenu}
            closeMenu={closeTOAMenu}
          />
        </div>
      )
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

export default connect(mapStateToProps, { loadTOA })(TOAPage);
