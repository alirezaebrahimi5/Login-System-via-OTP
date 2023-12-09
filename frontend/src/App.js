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
        <nav>
          <ul>
            <li><Link to="/">Home</Link></li>
            <li><Link to="/login">Login</Link></li>
            <li><Link to="/password-change">Change Password</Link></li>
            <li><Link to="/verify-token">Verify Token</Link></li>
          </ul>
        </nav>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="login" element={<Login />} />
          <Route path="password-change" element={<PasswordChange />} />
          <Route path="verify-token" element={<VerifyToken />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
