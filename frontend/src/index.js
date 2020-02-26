import React from "react";
import ReactDOM from "react-dom";
import FirstComponent from './components/FirstComponent';

const wrapper = document.getElementById('container');
wrapper ? ReactDOM.render(<FirstComponent />, wrapper) : console.log('no container found');
