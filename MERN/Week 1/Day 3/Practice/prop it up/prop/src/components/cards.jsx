import React from "react"

const PersonCard = (props) =>{
    console.log(props)
    return(
        <div>
            <h1>{props.firstName},{props.lastName}</h1>
            <h2>age : {props.age}</h2>
            <h2>age : {props.hairColor}</h2>

        </div>
    )
}
export default PersonCard 