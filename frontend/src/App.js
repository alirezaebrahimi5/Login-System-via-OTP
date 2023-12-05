import './App.css';
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from './components/Home';
import Login from './components/Login';
import PasswordChange from './components/PasswordChange';
import VerifyToken from './components/VerifyToken';

function App() {
  return (
    <div className="App">
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/password-change" element={<PasswordChange />} />
        <Route path="/token/verify/" element={<VerifyToken />} />
        {/* Add more routes for other components here */}
      </Routes>
    </div>
  );
}

export default App;
