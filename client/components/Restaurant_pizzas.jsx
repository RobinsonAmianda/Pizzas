import React,  { useState, useEffect } from 'react'

function Restaurant_pizzas() {
    const [restaurant_pizzas, setRestaurant_pizzas] = useState([]);
    
    useEffect(() => {
      fetch('http://127.0.0.1:5000/restaurant_pizzas')
      .then((res) => res.json())
      .then((data) =>console.log(data))
    }, []);
  
    return (
      <div> 
         {restaurant_pizzas} 
      </div>
    )
  }

export default Restaurant_pizzas
