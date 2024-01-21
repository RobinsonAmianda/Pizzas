import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import Restaurant from '../components/Restaurant'
import Pizza from '../components/Pizza'
import Restaurant_pizzas from '../components/Restaurant_pizzas'



ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
    <Restaurant/> 
     <Pizza/> 
     <Restaurant_pizzas/>


  </React.StrictMode>,
)
