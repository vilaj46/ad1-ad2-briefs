import React from "react";
import { connect } from "react-redux";

import LargeBriefForm from "../UploadPage/BriefForm/LargeBriefForm";
import prepareOutputFile from "../../../actions/reviewPage/prepareOutputFile.js";
import createOutputFile from "../../../actions/reviewPage/createOutputFile.js";

import styles from "./ReviewPage.module.css";
import PageList from "./PageList";

class ReviewPage extends React.Component {
  state = {
    output: "",
    arePagesLoaded: false,
  };

  componentDidMount = () => {
    const { toc, toa, cover } = this.props;
    const arePagesLoaded = toc.loaded || toa.loaded || cover.loaded;

    this.setState({ arePagesLoaded });
  };

  onClick = () => {
    const { arePagesLoaded } = this.state;
    const { prepareOutputFile, createOutputFile } = this.props;
    if (arePagesLoaded === false) {
      prepareOutputFile().then(() => {
        this.setState({ arePagesLoaded: true });
      });
    } else {
      createOutputFile();
    }
  };

  render() {
    const { brief, checklist } = this.props;
    const { arePagesLoaded } = this.state;

    return brief.filePath.length === 0 ? (
      <LargeBriefForm />
    ) : (
      <div className={styles.grid}>
        <div className={styles.buttons}>
          <div>
            <button
              type="button"
              onClick={this.onClick}
              className={`${
                arePagesLoaded === false ? styles.show : styles.hide
              } ${styles.filelabel}`}
            >
              Prepare Output File
            </button>
            <button
              type="button"
              onClick={this.onClick}
              className={`${
                arePagesLoaded === false ? styles.hide : styles.show
              } ${styles.filelabel}`}
            >
              Create Output File
            </button>
          </div>
          <p className={styles.output}>
            {brief.outputPath.length > 0
              ? "File created at: \n" + brief.outputPath
              : "Output file path will go here."}
          </p>
        </div>
        <PageList checks={checklist[0]} page={0} />
        <PageList checks={checklist[1]} page={1} />
        <PageList checks={checklist[2]} page={2} />
        <PageList checks={checklist[3]} page={3} />
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  const { brief, cover, toc, toa, checklist } = state;
  if (brief && Object.keys(brief).length > 0) {
    return {
      brief,
      cover,
      toc,
      toa,
      checklist,
    };
  } else {
    return {
      brief: { filePath: "", outputPath: "" },
      cover: {},
      toc: {},
      toa: {},
      checklist: [],
    };
  }
};

export default connect(mapStateToProps, {
  prepareOutputFile,
  createOutputFile,
})(ReviewPage);
