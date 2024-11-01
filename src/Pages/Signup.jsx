import { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

function SignUp() {
  const [username, setUsername] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [userId, setUserId] = useState();
  const [message, setMessage] = useState("");

  const history = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      username,
      email,
      password,
    };

    const url = "http://127.0.0.1:5000/signup/create_user";

    const response = await axios.post(url, data);

    if (response.data.redirect_url) {
      history(response.data.redirect_url);
    } else {
      const data = await response.json();
      alert(data.message);
    }
  };

  const handleDelete = async (e) => {
    e.preventDefault();
    try {
      axios.delete(`http://127.0.0.1:5000/signup/delete_user/${userId}`);
    } catch (error) {
      setMessage("Error: " + error.message);
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
      <br />
      <form onSubmit={handleDelete}>
        <div>
          <label htmlFor="delete">User Id</label>
          <input
            type="number"
            required
            onChange={(e) => setUserId(e.target.value)}
          />
          <button type="submit">Delete User</button>
        </div>
      </form>

      <h1>{message}</h1>
    </>
  );
}

export default SignUp;
