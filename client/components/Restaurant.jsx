import React,  { useState, useEffect } from 'react'

function Restaurant() {
   const [restaurants, setRestaurants] = useState([]);
    
  useEffect(() => {
    fetch('http://127.0.0.1:5000/restaurants')
    .then((res) => res.json())
    .then((data) =>console.log(data))
  }, []);

  return (
    <div> 
       {restaurants} 
    </div>
  )
}

export default Restaurant
