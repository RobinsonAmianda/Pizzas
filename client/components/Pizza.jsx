import React,  { useState, useEffect } from 'react'

function Pizza() {
    const [data, setData] = useState([]);
    
  useEffect(() => {
    fetch('http://127.0.0.1:5000/pizzas')
    .then((res) => res.json())
    .then((data) =>setData(data))
  }, []);

  return (
    <div> 
       {data.map(pizzas=>(
        <div>
          <h3>Name:${pizzas.name}</h3>
          <h3>Ingredients:{pizzas.Ingredients}</h3>
          
        </div>
       ))} 
    </div>
  )
}

export default Pizza