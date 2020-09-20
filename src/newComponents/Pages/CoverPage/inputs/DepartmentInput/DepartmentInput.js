import React from "react";
import { connect } from "react-redux";
import styles from "./DepartmentInput.module.css";
import changeDepartment from "../../../../../actions/coverPage/changeDepartment";

class DepartmentInput extends React.Component {
  state = {
    displayDropdown: false,
  };

  onMouseEnter = () => {
    this.setState({ displayDropdown: true });
  };

  onMouseLeave = () => {
    this.setState({ displayDropdown: false });
  };

  closeDropdown = () => this.setState({ displayDropdown: false });

  render() {
    const { displayDropdown } = this.state;
    const { department, changeDepartment } = this.props;
    const errorStyle = department.error ? styles.error : "";
    return (
      <form
        className={styles.departmentForm}
        onMouseEnter={this.onMouseEnter}
        onMouseLeave={this.onMouseLeave}
        id="departmentInput"
      >
        <p className={styles.appellateDivision}>
          Appellate Division -{" "}
          <span className={errorStyle}>{department.text || "________"}</span>{" "}
          Department
        </p>
        <div className={styles.departmentDivider} />
        <DepartmentDropdown
          display={displayDropdown}
          changeDepartment={changeDepartment}
          closeDropdown={this.closeDropdown}
        />
      </form>
    );
  }
}

const DepartmentDropdown = ({ display, changeDepartment, closeDropdown }) => {
  const courts = ["First", "Second"];

  const onClick = (court) => {
    changeDepartment(court);
    closeDropdown();
  };

  const displayStyle = display ? styles.displayDropdown : "";

  return (
    <div className={`${styles.dropdown} ${displayStyle}`}>
      {courts.map((court) => (
        <li
          key={court}
          className={styles.dropdownItem}
          onClick={() => onClick(court)}
        >
          {court}
        </li>
      ))}
    </div>
  );
};

const mapStateToProps = (state) => {
  const { department } = state.cover;

  if (department) {
    return { department };
  } else {
    return {
      department: {
        text: "",
        error: true,
      },
    };
  }
};

export default connect(mapStateToProps, { changeDepartment })(DepartmentInput);
