import React from "react";
import { Link, useMatch, useResolvedPath } from "react-router-dom";

const Navbar = () => {
  return (
    <>
      <nav className="nav">
        <Link to="/" className="sitetitle">
          Site Name
        </Link>
        <ul>
          <CustomeLink to="/time">Time</CustomeLink>
          <CustomeLink to="/login">Login</CustomeLink>
          <CustomeLink to="/signup">Signup</CustomeLink>
          <CustomeLink to="/leaderboard">Leaderboard</CustomeLink>
          <CustomeLink to="/store">Store</CustomeLink>
          <CustomeLink to="/quest">Quest</CustomeLink>
          <CustomeLink to="/skills">Skills</CustomeLink>
          <CustomeLink to="/upload">Upload</CustomeLink>
        </ul>
      </nav>
    </>
  );
};

function CustomeLink({ to, children, ...props }) {
  const resolvedPath = useResolvedPath(to);
  const isActive = useMatch({ path: resolvedPath.pathname, end: true });

  return (
    <li className={isActive ? "active" : ""}>
      <Link to={to} {...props}>
        {children}
      </Link>
    </li>
  );
}

export default Navbar;
