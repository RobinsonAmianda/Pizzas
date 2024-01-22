import React,  { useState, useEffect } from 'react'

function Restaurant() {
   const [data, setData] = useState([]);
    
  useEffect(() => {
    fetch('http://127.0.0.1:5000/restaurants')
    .then((res) => res.json())
    .then((data) =>console.log(data))
  }, []);

  return (
    <div> 
       {data.map(restaurants=>(
        <div>
          <h3>Name:${restaurants.name}</h3>
          <h3>Address:{restaurants.address}</h3>
          
        </div>
       ))} 
    </div>
  )
}

export default Restaurant
