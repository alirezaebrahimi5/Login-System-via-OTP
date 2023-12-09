import { createStore, combineReducers, applyMiddleware } from "redux";
import thunk from "redux-thunk";
import userLoginReducer from "./reducers/userReducer";

const reducer = combineReducers({ userLogin: userLoginReducer });

const userInfoFromStorage = localStorage.getItem("userInfo")
  ? JSON.parse(localStorage.getItem("userInfo"))
  : null;

const initialState = { userInfo: { userInfoFromStorage } };

const store = createStore(reducer, initialState);

export default store;
