import React from "react";

const Display = (props)=>{

    console.log(props.user);
    return(
        <div>
            <h1>welcome</h1>
            <h2>First Name :{props.user.firstName}</h2> 
            <h2>Last Name {props.user.lastName}</h2> 
            <h2>Email {props.user.Email}</h2> 
            <h2>Password {props.user.Password}</h2> 
            <h2>Confirm Password {props.user.Confirmpass}</h2> 
        </div>
    )
}
export default Display