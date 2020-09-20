import React from "react";

import styles from "./FileEntry.module.css";

import FileName from "./FileName";

class FileEntry extends React.Component {
  render() {
    const { data } = this.props;
    return (
      <div className={styles.fileEntryContainer}>
        <FileName data={data} />
      </div>
    );
  }
}

export default FileEntry;
