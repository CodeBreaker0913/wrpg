import React from "react";
import { Routes, Route } from "react-router-dom";

import Time from "./Pages/Time.jsx";
import Home from "./Home.jsx";
import Login from "./Pages/Login.jsx";
import Navbar from "./Navbar.jsx";
import SignUp from "./Pages/Signup.jsx";

function App() {
  return (
    <>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/time" element={<Time />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<SignUp />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
