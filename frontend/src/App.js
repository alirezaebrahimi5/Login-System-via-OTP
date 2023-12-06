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
      <Route path='/' Component={Home} exact />
      <Route path='/login' Component={Login} />
      <Route path='/password-change' Component={PasswordChange} />
      <Route path='/verify-token' Component={VerifyToken} />
      </BrowserRouter>
      
      <h1>
        App components
      </h1>
    </div>
  );
}

export default App;
