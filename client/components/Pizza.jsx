import React,  { useState, useEffect } from 'react'

function Pizza() {
    const [data, setData] = useState([]);
    
  useEffect(() => {
    fetch('http://127.0.0.1:5000/pizzas')
    .then((res) => res.json())
    .then((data) => setData(data))
  }, []);
  return (
    <div> 
        <h2>PIZZA IN TOWN</h2>
        
            <ol>1.Cheese Pizza.</ol>
            <ol>2.Veggie Pizza.</ol>
            <ol>3.Pepperoni Pizza.</ol>
            <ol>4.Meat Pizza.</ol>
            <ol>5.Hawaiian Pizza</ol>
        
        {
            data.map(pizzas=>{
                return(
                    <div>
                    <h2>{pizzas.name}</h2>
                    <p>{pizzas.ingredients}</p>
                    </div>
                )
            })
        }
    </div>
  )
}

export default Pizza