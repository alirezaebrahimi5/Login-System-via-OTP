import React, { useState, useEffect } from "react";
import { Form, Button } from "react-bootstrap";
import { useSelector, useDispatch } from "react-redux";
import login from "../actions/userActions";

function Login(location, history) {
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");

  const dispatch = useDispatch();

  const userLogin = useSelector((state) => state.userLogin);

  const redirect = location.search ? location.search.split("=")["1"] : "/";

  const { error, userInfo, loading } = userLogin;

  useEffect(() => {
    if (userInfo) {
      history.push(redirect);
    }
  }, [history, userInfo, redirect]);

  const submitHandler = (e) => {
    e.preventDefault();
    dispatch(login(phone, password));
  };

  return (
    <div>
      <h1>Login Form</h1>
      <form method="post">
        <Form onSubmit={submitHandler}>
          <Form.Group controlId="Phone">
            <Form.Label>Phone Number</Form.Label>
            <Form.Control
              type="phone"
              placeholder="Enter your phone number"
              value={phone}
              onChange={(e) => setPhone(e.target.value)}
            ></Form.Control>
          </Form.Group>

          <Form.Group controlId="Password">
            <Form.Control
              type="password"
              placeholder="Enter your password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            ></Form.Control>
          </Form.Group>

          <Button type="submit" variant="primary">
            Login
          </Button>
        </Form>
      </form>
    </div>
  );
}

export default Login;
