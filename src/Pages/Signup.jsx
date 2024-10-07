function SignUp() {
  return (
    <>
      <h3>Signup</h3>
      <div>
        <label for="username">Username</label>
        <input
          type="username"
          className="form-control"
          id="username"
          name="username"
          placeholder="Enter username"
        ></input>
      </div>
      <div>
        <label for="email">Email Address</label>
        <input
          type="email"
          className="form-control"
          id="email"
          name="email"
          placeholder="Enter email"
        ></input>
      </div>
      <div>
        <label for="password1">Password</label>
        <input
          type="password"
          className="form-control"
          id="password1"
          name="password1"
          placeholder="Enter password"
        ></input>
      </div>
      <div>
        <label for="password2">Confirm Password</label>
        <input
          type="password"
          className="form-control"
          id="password2"
          name="password2"
          placeholder="(Confirm)"
        ></input>
      </div>
      <br />
      <button type="submit">Signup</button>
    </>
  );
}

export default SignUp;
