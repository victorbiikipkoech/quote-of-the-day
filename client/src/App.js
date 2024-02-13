// App.js

import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import NavBar from './components/NavBar'; // Import the NavBar component
import LoginPage from './components/LoginPage';
import Signup from './components/Signup';
import HomePage from './components/HomePage'; // Import the HomePage component

const App = () => {
  return (
    <Router>
      <div>
        <NavBar /> {/* Include the NavBar component */}
        <Routes>
          <Route path="/" element={<HomePage />} /> {/* Define a route for the root URL */}
          <Route path="/login" element={<LoginPage />} />
          <Route path="/signup" element={<Signup />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
