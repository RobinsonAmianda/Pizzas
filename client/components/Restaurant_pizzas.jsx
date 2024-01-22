import React,  { useState, useEffect } from 'react'

function Restaurant_pizzas() {
    const [data, setData] = useState([]);
    
    useEffect(() => {
      fetch('http://127.0.0.1:5000/restaurant_pizzas')
      .then((res) => res.json())
      .then((data) =>setData(data))
    }, []);
  
    return (
      <div> 
         {data.map(restaurant_pizzas=>(
          <div>
            <h3>Price:${restaurant_pizzas.price}</h3>
            <h3>Pizza_id:{restaurant_pizzas.pizza_id}</h3>
            <h3>Restaurant_id:{restaurant_pizzas.restaurant_id}</h3>
          </div>
         ))} 
      </div>
    )
  }

export default Restaurant_pizzas
