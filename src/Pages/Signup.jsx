import { useState } from "react";
import axios from "axios";

function SignUp() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.get("http://127.0.0.1:5000/api/signup", {
        username,
        email,
        password,
      });
      setMessage(response.data.message);
    } catch (error) {
      setMessage(
        error.response ? error.response.data.message : "An error occurred"
      );
    }
  };

  return (
    <>
      <h3>Signup</h3>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="username">Username</label>
          <input
            type="text"
            className="form-control"
            id="username"
            name="username"
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Enter username"
            required
          />
        </div>
        <div>
          <label htmlFor="email">Email Address</label>
          <input
            type="email"
            className="form-control"
            id="email"
            name="email"
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter email"
            required
          />
        </div>
        <div>
          <label htmlFor="password1">Password</label>
          <input
            type="password"
            className="form-control"
            id="password1"
            name="password"
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter password"
            required
          />
        </div>
        <button type="submit">Signup</button>
      </form>

      <h1>{message}</h1>
    </>
  );
}

export default SignUp;
