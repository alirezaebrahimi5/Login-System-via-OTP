import './App.css';
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from './components/Home';
import Login from './components/Login';
import PasswordChange from './components/PasswordChange';
import VerifyToken from './components/VerifyToken';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      </BrowserRouter>
      
      <h1>
        App components
      </h1>
    </div>
  );
}

export default App;
