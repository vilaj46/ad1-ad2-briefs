import React from "react";
import { connect } from "react-redux";

import styles from "./FileEntries.module.css";

import FileEntry from "../FileEntry/FileEntry";
import Spotlight from "../Spotlight/Spotlight";

class FileEntries extends React.Component {
  render() {
    const { files } = this.props;
    setupGrid(files);
    return (
      files.length > 0 && (
        <div className={styles.filesContainer}>
          <div className={styles.entriesContainer}>
            {files.map((file) => {
              return <FileEntry data={file} key={file.IDNumber} />;
            })}
          </div>
          <Spotlight />
        </div>
      )
    );
  }
}

/**
 * setupGrid
 *
 * @param {Array} files
 *
 * When we select a file to open up in the spotlight, we want the spotlight to line
 * up with the file selected. This way, we do not need a fixed spotlight and
 * grid does not work with inline styles.
 *
 * We select the files container which will also hold the spotlight. Our
 * file list items are 40px so we just create the number of files in rows
 * at the 40px.
 */
function setupGrid(files) {
  const grid = document.querySelector(`.${styles.filesContainer}`);
  if (grid && files.length > 0) {
    grid.setAttribute(
      "style",
      `grid-template-rows: repeat(${files.length}, 40px)`
    );
  } else if (files.length > 0) {
    // Waits a millisecond for the page to load.
    setTimeout(() => {
      const grid = document.querySelector(`.${styles.filesContainer}`);
      grid.setAttribute(
        "style",
        `grid-template-rows: repeat(${files.length}, 40px)`
      );
    }, 100);
  }
}

const mapStateToProps = (state) => {
  const { uploads } = state;
  if (uploads && Object.keys(uploads).length > 0) {
    return {
      files: uploads.displayForFiles,
    };
  } else {
    return {
      files: [],
    };
  }
};

export default connect(mapStateToProps)(FileEntries);
