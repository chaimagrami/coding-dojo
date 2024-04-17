import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Home from './components/Home';
import CombinedPage from './components/CombinedPage';
import StyledWordPage from './components/StyledWordPage';
import './styles/styles.css'

function App() {
  return (
    <Routes>
      <Route path="/home" element={<Home />} />
      <Route path="/:param" element={<CombinedPage />} />
      <Route path="/:word/:textColor/:bgColor" element={<StyledWordPage />} />
      <Route path="*" element={<Home />} />
    </Routes>
  );
}

export default App;
