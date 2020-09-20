import React from "react";
import { connect } from "react-redux";

import styles from "./ContextMenu.module.css";
import removeTOCEntry from "../../actions/tocPage/removeTOCEntry.js";
import insertTOCEntry from "../../actions/tocPage/insertTOCEntry.js";
import removeTOAEntry from "../../actions/toaPage/removeTOAEntry.js";
import insertTOAEntry from "../../actions/toaPage/insertTOAEntry.js";
import removeTOCEntries from "../../actions/tocPage/removeTOCEntries.js";
import removeTOAEntries from "../../actions/toaPage/removeTOAEntries.js";

const ContextMenu = ({
  xPos,
  yPos,
  display,
  IDNumber,
  page,
  removeTOCEntry,
  insertTOCEntry,
  removeTOAEntry,
  insertTOAEntry,
  removeTOCEntries,
  removeTOAEntries,
}) => {
  /**
   * remove
   *
   * If we click the Remove Entry on the Table of Contents / Authorities page,
   * we remove the entry from the list with the action.
   */
  const remove = () => {
    if (page === 2) {
      removeTOCEntry(IDNumber);
    } else if (page === 3) {
      removeTOAEntry(IDNumber);
    } else {
      return;
    }
  };

  /**
   * insert
   *
   * @param {Number} direction - Where we want to insert a new entry.
   *
   * If we click the Insert Entry Above / Below on the Table of Contents / Authorities page,
   * we will insert the entry with the action.
   */
  const insert = (direction) => {
    if (page === 2) {
      insertTOCEntry(IDNumber, direction);
    } else if (page === 3) {
      insertTOAEntry(IDNumber, direction);
    } else {
      return;
    }
  };

  /**
   * removeAll
   *
   * If we click the Remove All on the Table of Contents / Authorities page,
   * we will delete all the entries with the action.
   */
  const removeAll = () => {
    if (page === 2) {
      removeTOCEntries();
    } else if (page === 3) {
      removeTOAEntries();
    } else {
      return;
    }
  };

  return (
    display && (
      <ul className={styles.menu} style={{ top: yPos, left: xPos }}>
        <div className={styles.itemContainer} onClick={() => insert(1)}>
          <li className={styles.item}>Insert Entry Above</li>
        </div>
        <div className={styles.itemContainer} onClick={() => insert(-1)}>
          <li className={styles.item}>Insert Entry Below</li>
        </div>
        <div className={styles.itemContainer} onClick={remove}>
          <li className={styles.item}>Remove Entry</li>
        </div>
        <hr />
        <div className={styles.itemContainer} onClick={removeAll}>
          <li className={styles.item}>Remove All</li>
        </div>
      </ul>
    )
  );
};

const mapStateToProps = (state) => {
  const { page } = state;
  return {
    page: page.active,
  };
};

export default connect(mapStateToProps, {
  removeTOCEntry,
  insertTOCEntry,
  removeTOAEntry,
  insertTOAEntry,
  removeTOAEntries,
  removeTOCEntries,
})(ContextMenu);
