import React, { useState, useEffect } from "react";
import { Form, Button } from "react-bootstrap";

function Login() {
  const [phone, setPhone] = useState("");
  const [password, setPassword] = useState("");

  const submitHandler = (e) => {
    e.preventDefault();
    console.log("form submitted");
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
