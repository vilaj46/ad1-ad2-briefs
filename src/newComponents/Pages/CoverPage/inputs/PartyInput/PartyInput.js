import React from "react";
import { connect } from "react-redux";

import styles from "./PartyInput.module.css";
import coverStyles from "../../CoverPage.module.css";
import changeParty from "../../../../../actions/coverPage/changeParty";

class PartyInput extends React.Component {
  state = {
    parties: {
      plaintiff: { text: "", error: true },
      defendant: { text: "", error: true },
    },
  };

  componentDidMount = () => {
    const { propParties } = this.props;
    this.setState({ parties: propParties });
  };

  onChange = (e) => {
    const { changeParty } = this.props;
    const { parties } = this.state;

    this.setState({
      parties: {
        ...parties,
        [e.target.name]: {
          ...parties[e.target.name],
          text: e.target.value,
        },
      },
    });

    changeParty(e);
  };

  render() {
    const { party, propParties } = this.props;
    const { parties } = this.state;
    const errorStyle = propParties[party].error ? styles.error : "";
    return (
      <form className={coverStyles.form}>
        <input
          className={`${coverStyles.textInput} ${errorStyle}`}
          type="text"
          name={party}
          value={parties[party].text}
          placeholder={party}
          onChange={(e) => this.onChange(e)}
          id={`${party}Input`}
        />
      </form>
    );
  }
}

const mapStateToProps = (state) => {
  const { plaintiff, defendant } = state.cover;
  if (plaintiff !== undefined && defendant !== undefined) {
    return {
      propParties: {
        plaintiff,
        defendant,
      },
    };
  } else {
    return {
      propParties: {
        plaintiff: { text: "", error: true },
        defendant: { text: "", error: true },
      },
    };
  }
};

export default connect(mapStateToProps, { changeParty })(PartyInput);
