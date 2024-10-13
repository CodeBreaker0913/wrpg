function Login() {
  return (
    <>
      <form method="POST">
        <h3>LOGIN</h3>
        <div>
          <label htmlFor="username">Username</label>
          <input
            type="username"
            className="form-control"
            id="username"
            name="username"
            placeholder="Enter username"
          ></input>
        </div>
        <div>
          <label htmlFor="password">Password</label>
          <input
            type="password"
            className="form-control"
            id="password"
            name="password"
            placeholder="Enter password"
          ></input>
        </div>
        <br />
        <button type="submit">Login</button>
      </form>
    </>
  );
}

export default Login;
