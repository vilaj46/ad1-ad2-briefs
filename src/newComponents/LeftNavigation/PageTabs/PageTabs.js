import React from "react";
import { connect } from "react-redux";

import styles from "./Pages.module.css";
import changePage from "../../../actions/changePage.js";

const PageTabs = ({ activePage, changePage, checklist }) => {
  return (
    <div className={styles.main}>
      {checklist.map((obj, index) => (
        <Tab
          text={obj.text}
          key={obj.text}
          label={obj.label}
          activePage={activePage}
          index={index}
          changePage={changePage}
        />
      ))}
    </div>
  );
};

const Tab = ({ text, label, activePage, index, changePage }) => {
  const activeStyle = activePage === index ? styles.active : "";
  return (
    <li
      className={`${styles.stepContainer} ${activeStyle}`}
      title={text}
      onClick={() => changePage(index)}
    >
      {label}
    </li>
  );
};

const mapStateToProps = (state) => {
  const { checklist, page } = state;
  return { activePage: page.active, checklist };
};

export default connect(mapStateToProps, {
  changePage,
})(PageTabs);
