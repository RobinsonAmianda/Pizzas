import React,  { useState, useEffect } from 'react'

function Restaurant() {
   const [data, setData] = useState([]);
    
  useEffect(() => {
    fetch('http://127.0.0.1:5000/restaurants')
    .then((res) => res.json())
    .then((data) => setData(data))
  }, []);

  return (
    <div> 
        <h2>WELCOME TO OUR RESTAURANTS</h2>
        <h5>1.Villa Rosa_Kempinski</h5>
        <h5>2.Malvida kalinsky 001</h5>
        <h5>3.Mombasa Raha Cafe</h5>
        <h5>4.Kay Restaurant chill</h5>
        <h5>5.Nairobi Street Kitchen</h5>
        {
            data.map(restaurant=>{
                return(
                    <div>
                    <h2>{restaurant.name}</h2>
                    <p>{restaurant.address}</p>
                    </div>
                )
            })
        }
    </div>
  )
}

export default Restaurant