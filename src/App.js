import React, {useState,useEffect,useContext} from 'react';
import logo from './logo.svg';
import './App.css';
import MainForm from './components/Form'
// import {
//   BrowserRouter as Router,
//   Switch,
//   Route,
//   Link
// } from "react-router-dom";

function App() { 

  return (
    <div className="App">
        <h1>Translator App</h1>
        <MainForm/>
    </div>
  );
}

export default App;
