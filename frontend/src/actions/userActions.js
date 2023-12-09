import axios from "axios";
import {
  USER_LOGIN_REQUEST,
  USER_LOGIN_SUCCESS,
  USER_LOGIN_FAIL,
  USER_LOGOUT,
  USER_PASSWORD_CHANGE_FAIL,
  USER_PASSWORD_CHANGE_SUCCESS,
  
  USER_PASSWORD_CHANGE,
} from "../constants/userConstants";

const login = (phone, password) => async (dispatch) => {
  try {
    dispatch({
      type: USER_LOGIN_REQUEST,
    });

    const config = {
      headers: {
        "Content-type": "application-json",
      },
    };

    const { data } = await axios.post(
      "http://127.0.0.1:8000/user/login",
      {
        phone: phone,
        password: password,
      },
      config
    );

    dispatch({
      type: USER_LOGIN_SUCCESS,
      payload: data,
    });

    localStorage.setItem("userInfo", JSON.stringify(data));
  } catch (error) {
    dispatch({
      type: USER_LOGIN_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};

const reset = (old_password, new_password) => async (dispatch) => {
  try {
    dispatch({
      type: USER_PASSWORD_CHANGE,
    });

    const config = {
      headers: {
        "Content-type": "application-json",
      },
    };

    const { data } = await axios.post(
      "http://127.0.0.1:8000/user/reset",
      {
        old_password: old_password,
        new_password: new_password,
      },
      config
    );

    dispatch({
      type: USER_PASSWORD_CHANGE_SUCCESS,
      payload: data,
    });

    localStorage.setItem("userInfo", JSON.stringify(data));
  } catch (error) {
    dispatch({
      type: USER_PASSWORD_CHANGE_FAIL,
      payload:
        error.response && error.response.data.detail
          ? error.response.data.detail
          : error.message,
    });
  }
};


export {login, reset};