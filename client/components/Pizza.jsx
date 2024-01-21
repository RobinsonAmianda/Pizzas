import React,  { useState, useEffect } from 'react'

function Pizza() {
    const [pizzas, setPizzas] = useState([]);
    
  useEffect(() => {
    fetch('http://127.0.0.1:5000/pizzas')
    .then((res) => res.json())
    .then((data) =>console.log(data))
  }, []);

  return (
    <div> 
       {pizzas} 
    </div>
  )
}

export default Pizza