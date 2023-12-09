import React, { useState, useEffect } from "react";
import { Form, Button } from "react-bootstrap";
import { useSelector, useDispatch } from "react-redux";
import {reset} from "../actions/userActions";

function Reset(location, history) {
  const [newPassword, setNewPassword] = useState("");
  const [oldPassword, setOldPassword] = useState("");

  const dispatch = useDispatch();

  const userLogin = useSelector((state) => state.userLogin);

  const redirect = location.search ? location.search.split("=")[1] : "/";

  const { error, userInfo, loading } = userLogin;

  useEffect(() => {
    if (userInfo) {
      history.push(redirect);
    }
  }, [history, userInfo, redirect]);

  const submitHandler = (e) => {
    e.preventDefault();
    dispatch(reset(oldPassword, newPassword));
  };

  return (
    <div>
      <h1>Reset Form</h1>
      <form method="post">
        <Form onSubmit={submitHandler}>
          {error && <h1> {error} </h1>}
          <Form.Group controlId="old_password">
            <Form.Label>old password</Form.Label>
            <Form.Control
              type="password"
              placeholder="Enter your old password"
              value={oldPassword}
              onChange={(e) => setOldPassword(e.target.value)}
            ></Form.Control>
          </Form.Group>

          <Form.Group controlId="new_password">
            <Form.Control
              type="password"
              placeholder="Enter new password"
              value={newPassword}
              onChange={(e) => setNewPassword(e.target.value)}
            ></Form.Control>
          </Form.Group>

          <Button type="submit" variant="primary">
            Reset
          </Button>
        </Form>
      </form>
    </div>
  );
}

export default Reset;
