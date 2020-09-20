import React from "react";

import styles from "./TOAEntries.module.css";

class TOAEntry extends React.Component {
  state = {
    text: "",
    pageNumberInPdf: "",
  };

  componentDidMount = () => {
    const { entry } = this.props;
    this.setState({
      text: entry.entry,
      pageNumberInPdf: entry.pageNumberInPdf || -1,
    });
  };

  componentWillUnmount = () => {
    this.setState({
      text: "",
      padNumberInPdf: "",
    });
  };

  onRightClick = (e) => {
    const { index, setMenuPosition, setEntrySelected, entry } = this.props;
    const elements = document.querySelectorAll(`.${styles.toaEntry}`);
    const totalHeights = this.getTotalHeights(elements);
    // The x is already relative to the page. The div is slightly off, so we have to correct
    // once we style the dropdown menu.
    // The y is way more complicated. The 84 comes from the top of the page to the top of the container of entries.
    // The 59 is the height of each entry. The index is the position in the grid.
    // So our forumal needs to take into account for all of these because our pageX and pageY don't work.
    const x = e.nativeEvent.offsetX;
    const y = e.nativeEvent.offsetY;
    const yPos = y + totalHeights[index];
    setMenuPosition(x, yPos);
    setEntrySelected(entry.id);
  };

  getTotalHeights = (elements) => {
    let totals = [];

    elements.forEach((element, index) => {
      let total = 0;
      for (let i = 0; i <= index; i++) {
        total += elements[i].offsetHeight;
      }
      totals.push(total + 40 * index);
    });
    return totals;
  };

  onChange = (e) => {
    const { entry, changeEntry } = this.props;
    const { name, value } = e.target;

    if (name === "entry") {
      this.setState({ text: value });
    } else {
      this.setState({ pageNumberInPdf: value });
    }

    changeEntry({ name, value }, entry.id);
  };

  /**
   * calculateInitialRows
   *
   * @param {Object} e - Textarea
   *
   * On 1920 our max textarea width is 686.08. We can fit 58 chars about on the row.
   * Take our elements width multiple it by 58 and divide by the 686.08. This gives
   * us the max characters for that element width. We then find the amount of rows.
   */
  calculateInitialRows = () => {
    const { entry } = this.props;
    const { text } = this.state;
    const textarea = document.getElementById(`${entry.id}`);
    if (textarea) {
      const width = textarea.clientWidth;
      const maxCharPerLine = (width * 40) / 686.08;
      const rows = Math.ceil(text.length / maxCharPerLine);
      return rows;
    }
  };

  render() {
    const { entry } = this.props;
    const errorStyle =
      entry.entryTextError || entry.entryNumberError ? styles.error : "";
    const entryTextError = entry.entryTextError ? "entryTextHighlight" : "";
    const entryNumberError = entry.entryNumberError
      ? "entryNumberHighlight"
      : "";
    const { text, pageNumberInPdf } = this.state;
    return (
      <li
        key={entry.id}
        id={entry.id}
        className={`${styles.toaEntry} ${errorStyle}`}
        onContextMenu={(e) => this.onRightClick(e)}
      >
        <textarea
          className={`${styles.entryText} ${entryTextError} entryTOATextHighlight`}
          type="text"
          name="entry"
          value={text}
          onChange={(e) => this.onChange(e)}
          placeholder="Entry text goes here..."
          rows={this.calculateInitialRows()}
        />
        <textarea
          className={`${styles.entryNumber} ${entryNumberError} entryTOANumberHighlight`}
          type="text"
          name="pageNumberInPdf"
          value={pageNumberInPdf}
          onChange={(e) => this.onChange(e)}
          placeholder="#"
        />
      </li>
    );
  }
}

export default TOAEntry;
