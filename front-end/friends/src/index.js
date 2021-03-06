import React, {Fragment} from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import Detail from './Detail';
import reportWebVitals from './reportWebVitals';
import { BrowserRouter as Router, Routes, Route} from "react-router-dom";

const Routing = () => {
  return(
    <Router>
   <Fragment>
        <Routes>
          <Route exact path='/' element={<App/>}/>
          <Route exact path='/detail/:id' element={<Detail/>}/>
        </Routes>
      </Fragment>
  </Router>
  )
}

ReactDOM.render(
  <React.StrictMode>
    <Routing />
  </React.StrictMode>,
  document.getElementById('root')
);


// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
