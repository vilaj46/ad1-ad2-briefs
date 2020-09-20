import React from "react";
import { connect } from "react-redux";

import styles from "./TOAEntries.module.css";
import ContextMenu from "../../../ContextMenu/ContextMenu";
import changeEntry from "../../../../actions/toaPage/changeEntry.js";
import TOAEntry from "./TOAEntry";

class TOCEntries extends React.Component {
  state = {
    xPos: false,
    yPos: false,
    entrySelected: "",
  };

  setMenuPosition = (xPos, yPos) => {
    const { displayMenu } = this.props;
    this.setState({ xPos, yPos });
    displayMenu();
  };

  setEntrySelected = (entryID) => this.setState({ entrySelected: entryID });

  // removeEntrySelected = (entryID) => this.setState({ entrySelected: {} });

  render() {
    const { entries, showMenu, closeMenu, changeEntry } = this.props;
    const { xPos, yPos, entrySelected } = this.state;
    setupGrid(entries);
    return (
      <div className={styles.container}>
        <ul className={styles.toaEntries}>
          {entries.map((entry, index) => {
            return (
              <TOAEntry
                key={entry.id}
                entry={entry}
                setMenuPosition={this.setMenuPosition}
                index={index}
                setEntrySelected={this.setEntrySelected}
                changeEntry={changeEntry}
              />
            );
          })}
        </ul>
        {showMenu && (
          <ContextMenu
            xPos={xPos}
            yPos={yPos}
            display={showMenu}
            onClick={closeMenu}
            IDNumber={entrySelected}
          />
        )}
      </div>
    );
  }
}

const mapStateToProps = (state) => {
  const { entries } = state.toa;
  if (entries !== undefined) {
    return {
      entries,
    };
  } else {
    return {
      entries: [],
    };
  }
};

/**
 *
 * @param {*} entries
 */
function setupGrid(entries) {
  const grid = document.querySelector(`.${styles.toaEntries}`);
  if (grid && entries.length > 0) {
    grid.setAttribute(
      "style",
      `grid-template-rows: repeat(${entries.length}, 1fr)`
    );
  } else if (entries.length > 0) {
    // Waits a millisecond for the page to load.
    setTimeout(() => {
      const grid = document.querySelector(`.${styles.toaEntries}`);
      grid.setAttribute(
        "style",
        `grid-template-rows: repeat(${entries.length}, 1fr)`
      );
    }, 100);
  }
}

export default connect(mapStateToProps, { changeEntry })(TOCEntries);
