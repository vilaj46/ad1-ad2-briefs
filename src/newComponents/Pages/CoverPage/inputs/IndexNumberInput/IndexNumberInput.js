import React from "react";
import { connect } from "react-redux";

import styles from "./IndexNumberInput.module.css";
import coverStyles from "../../CoverPage.module.css";
import changeIndexNumber from "../../../../../actions/coverPage/changeIndexNumber";

class IndexNumberInput extends React.Component {
  state = {
    indexNumber: {
      formatted: "",
      unformatted: "",
      number: "",
      year: "",
      yearError: true,
      indexError: true,
    },
  };

  componentDidMount = () => {
    const { indexNumber } = this.props;
    this.setState({
      indexNumber: { ...indexNumber },
    });
  };

  /**
   * Currently bugged when it is not updated properly.
   * The caret is moved to the end on the re-render.
   *
   * @param {Object} prevProps
   * @param {Object} prevState
   */
  componentDidUpdate = (prevProps, prevState) => {
    Object.keys(prevProps.indexNumber).forEach((k) => {
      if (
        prevProps.indexNumber[k] !== this.props.indexNumber[k] ||
        prevState.indexNumber[k] !== this.state.indexNumber[k]
      ) {
        this.setState({
          indexNumber: { ...this.props.indexNumber },
        });
      }
    });
  };

  onChange = (e) => {
    const { changeIndexNumber } = this.props;
    this.setState({
      indexNumber: {
        ...this.state.indexNumber,
        [e.target.name]: e.target.value,
      },
    });

    changeIndexNumber(e);
  };

  render() {
    const { indexNumber } = this.state;
    const { number, year } = indexNumber;
    const indexNumberBorder = calculateIndexNumberBorder(indexNumber);
    const yearBorder = calculateYearBorder(indexNumber);
    return (
      <form className={coverStyles.three}>
        <div>
          <input
            name="number"
            type="text"
            required
            value={number}
            placeholder="Index Number"
            className={`${coverStyles.textInput} ${styles.input} ${indexNumberBorder}`}
            onChange={(e) => this.onChange(e)}
            id="indexNumberInput"
          />
          <input
            name="year"
            type="text"
            required
            placeholder="Year"
            value={year}
            className={`${styles.input} ${coverStyles.textInput} ${yearBorder}`}
            onChange={(e) => this.onChange(e)}
            id="yearInput"
          />
        </div>
      </form>
    );
  }
}

/**
 * calculateIndexNumberBorder
 *
 * @param {Object} indexNumber
 * @return {String} Style that we are going to use for the border.
 *
 * If there is no error, don't use any style.
 * If there is an error only with the index number portion, use the full border.
 * If there is an issue with both, use the partial border.
 *
 */
const calculateIndexNumberBorder = (indexNumber) => {
  const { indexError, yearError } = indexNumber;
  if (indexError === false) {
    return "";
  } else if (indexError && yearError) {
    return styles.topIsland;
  } else {
    return styles.error;
  }
};

/**
 * calculateYearBorder
 *
 * @param {Object} indexNumber
 * @return {String} Style that we are going to use for the border.
 *
 * If there is no error, don't use any style.
 * If there is an error only with the year portion, use the full border.
 * If there is an issue with both, use the partial border.
 *
 */
const calculateYearBorder = (indexNumber) => {
  const { indexError, yearError } = indexNumber;
  if (yearError === false) {
    return "";
  } else if (indexError && yearError) {
    return styles.bottomIsland;
  } else {
    return styles.error;
  }
};

const mapStateToProps = (state) => {
  const { indexNumber } = state.cover;
  if (indexNumber) {
    return { indexNumber };
  } else {
    return {
      indexNumber: {
        formatted: "",
        unformatted: "",
        number: "",
        year: "",
        yearError: true,
        indexError: true,
      },
    };
  }
};

export default connect(mapStateToProps, { changeIndexNumber })(
  IndexNumberInput
);
