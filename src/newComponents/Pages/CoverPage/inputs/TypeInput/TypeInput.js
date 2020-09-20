import React from "react";
import { connect } from "react-redux";

import styles from "./TypeInput.module.css";
import coverStyles from "../../CoverPage.module.css";
import changeTypeOfBrief from "../../../../../actions/coverPage/changeTypeOfBrief";

const TypeInput = ({ type, changeTypeOfBrief }) => {
  const choices = ["appbrief", "respbrief", "replybrief"];
  const errorStyle = type.error ? styles.error : "";
  return (
    <form className={`${coverStyles.two} ${errorStyle} `} id="typeInput">
      {choices.map((c, index) => {
        const firstStyle = index === 0 ? styles.first : "";
        const lastStyle = index === choices.length - 1 ? styles.last : "";
        const checked = c === type.text ? true : false;
        return (
          <li
            className={`${styles.choice} ${firstStyle} ${lastStyle}`}
            key={c}
            onClick={() => changeTypeOfBrief(c)}
          >
            <input
              type="radio"
              checked={checked}
              className={styles.typeInput}
              onChange={() => {
                return;
              }}
            />
            <label className={styles.label}>{c}</label>
          </li>
        );
      })}
    </form>
  );
};

const mapStateToProps = (state) => {
  const { type } = state.cover;
  if (type) {
    return { type };
  } else {
    return {
      type: {
        text: "",
        error: true,
      },
    };
  }
};

export default connect(mapStateToProps, { changeTypeOfBrief })(TypeInput);
