import React from "react";
import { connect } from "react-redux";

import styles from "./CoverPage.module.css";

import CoverHeader from "./CoverHeader/CoverHeader";
import LargeBriefForm from "../UploadPage/BriefForm/LargeBriefForm";
import PartyInput from "./inputs/PartyInput/PartyInput";
import DepartmentInput from "./inputs/DepartmentInput/DepartmentInput";
import IndexNumberInput from "./inputs/IndexNumberInput/IndexNumberInput";
import TypeInput from "./inputs/TypeInput/TypeInput";
import CoverOutput from "./CoverOutput/CoverOutput";
import CoverOptions from "./CoverOptions/CoverOptions";

import loadCover from "../../../actions/coverPage/loadCover";

class CoverPage extends React.Component {
  componentDidMount = () => {
    const { brief, loadCover, loaded } = this.props;
    if (brief.filePath.length > 0 && loaded === false) {
      loadCover();
    }
  };

  render() {
    const { brief } = this.props;
    return brief.filePath.length === 0 ? (
      <LargeBriefForm />
    ) : (
      <div className={styles.grid}>
        <CoverHeader />
        <div className={styles.one}>
          <DepartmentInput />
          <PartyInput party="plaintiff" />
          <p className={styles.against}>against</p>
          <PartyInput party="defendant" />
        </div>
        <TypeInput />
        <IndexNumberInput />
        <CoverOutput />
        <CoverOptions />
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  const { loaded } = state.cover;
  const { brief } = state;

  if (brief && Object.keys(brief).length > 0) {
    return {
      brief,
      loaded: loaded || false,
    };
  } else {
    return {
      brief: { filePath: "" },
      loaded: loaded || false,
    };
  }
};

export default connect(mapStateToProps, { loadCover })(CoverPage);
