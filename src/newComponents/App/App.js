import React from "react";
import { connect } from "react-redux";

import styles from "./App.module.css";

import LNContainer from "../LeftNavigation/LNContainer/LNContainer";
import UploadPage from "../Pages/UploadPage/UploadPage";
import CoverPage from "../Pages/CoverPage/CoverPage";
import TOCPage from "../Pages/TOCPage/TOCPage";
import TOAPage from "../Pages/TOAPage/TOAPage";
import ReviewPage from "../Pages/ReviewPage/ReviewPage";
import PDFContainer from "../PDFContainer/PDFContainer";
import TopError from "../TopError/TopError";

import syncFile from "../../actions/uploadPage/syncFile.js";

class App extends React.Component {
  state = {
    loaded: false,
    tocShowMenu: false,
    toaShowMenu: false,
  };

  openTOCMenu = () => this.setState({ tocShowMenu: true });

  closeTOCMenu = () => this.setState({ tocShowMenu: false });

  openTOAMenu = () => this.setState({ toaShowMenu: true });

  closeTOAMenu = () => this.setState({ toaShowMenu: false });

  /**
   * onClick
   *
   * Checks if our app is loaded so clicks are enabled. Also
   * checks if we have 'right-clicked' on our Table of Contents page.
   * We close our right click if it was open.
   */
  onClick = () => {
    const { loaded, tocShowMenu, toaShowMenu } = this.state;
    if (loaded && tocShowMenu) {
      this.closeTOCMenu();
    }
    if (loaded && toaShowMenu) {
      this.closeTOAMenu();
    }
  };

  /**
   * componentDidMount
   *
   * Initial load of our app. Will set the data properly from the backend since
   * we do not have any current state on the front end. Our setState either
   * enables or disables clicks on the app.
   */
  componentDidMount = () => {
    const { syncFile } = this.props;

    syncFile().then((res) => {
      this.setState({
        loaded: res,
      });
    });
  };

  /**
   * darkenBackground
   *
   * @return {String} - The darkenBackground className or an empty string.
   *
   * If we leave the upload page, check if there is a brief file uploaded.
   * If there is not, that means we cannot load the necessary information for that page.
   * We will then darken our background and display the LargeBriefForm.
   */
  darkenBackground = () => {
    const { brief, activePage } = this.props;
    let dark = false;

    try {
      if (brief === undefined || brief.filePath.length === 0) {
        dark = true;
      } else {
        dark = false;
      }
    } catch (err) {
      dark = true;
    }

    if (dark && activePage !== 0) {
      return styles.darkenBackground;
    } else {
      return "";
    }
  };

  /**
   * calculatePageWidth
   *
   * We want our UploadPage / ReviewPage to always be 95%.
   * If it is not our UploadPage it will be split with the PDF.
   */
  calculatePageWidth = () => {
    const { activePage, cover, uploads, brief } = this.props;
    if (
      activePage === 0 ||
      activePage === 4 ||
      (activePage === 1 && cover.numCoverPages === false) ||
      (activePage === 3 && Object.keys(uploads) === 0) ||
      (activePage === 3 && uploads.caseFiles.length === 0) ||
      brief.filePath.length === 0
    ) {
      return "95%";
    } else {
      return "";
    }
  };

  render() {
    const { activePage } = this.props;
    const { loaded, tocShowMenu, toaShowMenu } = this.state;
    const disabled = loaded === false ? styles.disabled : "";
    const darkened = this.darkenBackground();
    const width = this.calculatePageWidth();
    return (
      <div className={`${styles.main} ${disabled}`} onClick={this.onClick}>
        <LNContainer />
        <div className={styles.sub}>
          <div className={`${styles.page} ${darkened}`} style={{ width }}>
            <TopError />
            {activePage === 0 && <UploadPage />}
            {activePage === 1 && <CoverPage />}
            {activePage === 2 && (
              <TOCPage
                openTOCMenu={this.openTOCMenu}
                closeTOCMenu={this.closeTOCMenu}
                showMenu={tocShowMenu}
              />
            )}
            {activePage === 3 && (
              <TOAPage
                openTOAMenu={this.openTOAMenu}
                closeTOAMenu={this.closeTOAMenu}
                showMenu={toaShowMenu}
              />
            )}
            {activePage === 4 && <ReviewPage />}
          </div>
          <PDFContainer />
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  const { page, brief, cover, uploads } = state;
  if (brief) {
    return {
      brief,
      activePage: page.active,
      cover,
      uploads,
    };
  } else {
    return {
      brief: undefined,
      cover: undefined,
      activePage: page.active,
      uploads: {
        caseFiles: [],
      },
    };
  }
};

export default connect(mapStateToProps, { syncFile })(App);
