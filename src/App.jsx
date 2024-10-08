import React from "react";
import { Routes, Route } from "react-router-dom";

import Time from "./Pages/Time.jsx";
import Home from "./Home.jsx";
import Login from "./Pages/Login.jsx";
import Navbar from "./Navbar.jsx";
import SignUp from "./Pages/Signup.jsx";
import Leaderboard from "./Pages/Leaderboard.jsx";
import Store from "./Pages/Store.jsx";
import Quest from "./Pages/Quest.jsx";
import Skills from "./Pages/Skills.jsx";
import Upload from "./Pages/upload.jsx";

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
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/store" element={<Store />} />
          <Route path="/quest" element={<Quest />} />
          <Route path="/skills" element={<Skills />} />
          <Route path="/upload" element={<Upload />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
