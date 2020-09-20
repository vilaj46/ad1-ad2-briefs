import React from "react";
import { connect } from "react-redux";

import appStyles from "../../App/App.module.css";
import styles from "./Checklist.module.css";
import important_task from "../../../svgs/important_task.svg";

const Checklist = ({ checklist, activePage }) => {
  let lastClicked = {}; // Keep track to avoid highlight spam.

  /**
   * handleChecklistClick
   *
   * @param {String} id - location of our dom element.
   * @param {Number} time - milliseconds for the delay.
   *
   * Assign the time of when we clicked our checklist / associated id.
   * If we click the element again too early or are already highlighted, it will do nothing but avoiding the spam / time loop.
   * If we are ok with the click, it will select the dom element and invoke the highlightBorder function.
   * If we cannot find the dom element on the page, we catch our error and since it should be
   * the large brief form, we highlight that.
   */
  const handleChecklistClick = (id, time) => {
    const element = document.getElementById(id);
    try {
      if (
        Date.now() - lastClicked[id] < time ||
        Array.from(element.classList).includes(appStyles.highlightBorder)
      ) {
        return;
      }
    } catch {
      const uploadBrief = document.getElementById("uploadBrief");
      if ((element === null || id === "") && uploadBrief !== null) {
        if (Date.now() - lastClicked["uploadBrief"] < time) return;
        highlightBorderByElement(uploadBrief, time);
        lastClicked = { ...lastClicked, [id]: Date.now() };
        return;
      }
    }
    if (
      id === "entryTOCTextHighlight" ||
      id === "entryTOCNumberHighlight" ||
      id === "entryTOATextHighlight" ||
      id === "entryTOANumberHighlight"
    ) {
      const entries = document.querySelectorAll(`.${id}`);
      for (let i = 0; i < entries.length; i++) {
        highlightBorderByElement(entries[i], 2000);
      }
    } else if (id === "indexNumberInput") {
      const element2 = document.getElementById("yearInput");
      // Bugged, for some reason the inputs will not be highlighted.
      element.classList.toggle(appStyles.highlightBorder);
      element2.classList.toggle(appStyles.highlightBorder);
      setTimeout(() => {
        element.classList.toggle(appStyles.highlightBorder);
        element2.classList.toggle(appStyles.highlightBorder);
      }, time);
    } else {
      highlightBorderByElement(element, time);
    }
    lastClicked = { ...lastClicked, [id]: Date.now() };
  };

  /**
   * highlightBorderByElement
   *
   * @param {Element} element - The dom element we want to highlight.
   * @param {Number} time - milliseconds for the delay.
   *
   * We apply our class to the element and then remove it after the given seconds.
   */
  const highlightBorderByElement = (element, time) => {
    element.classList.toggle(appStyles.highlightBorder);

    setTimeout(() => {
      element.classList.toggle(appStyles.highlightBorder);
    }, time);
  };

  return (
    <ul className={styles.main}>
      {checklist[activePage].checklist.map((check) => {
        const applyLineThrough =
          check.completed === true ? styles.completed : "";
        return (
          <li
            key={check.id}
            className={`${styles.check} ${applyLineThrough}`}
            onClick={() => handleChecklistClick(check.id, 2000)}
          >
            <img
              className={styles.important}
              src={important_task}
              alt={check.id}
            />
            {check.element}
          </li>
        );
      })}
    </ul>
  );
};

const mapStateToProps = (state) => {
  const { page, checklist } = state;
  return {
    activePage: page.active,
    checklist: checklist,
  };
};

export default connect(mapStateToProps)(Checklist);
