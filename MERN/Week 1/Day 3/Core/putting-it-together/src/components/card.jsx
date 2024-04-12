import React from "react"
import { useState} from "react"




const PersonCard = (props) =>{


    const [newAge,setnewAge] = useState(props.age)

    const birth = () =>{
        setnewAge(newAge+1)
    }



    console.log(props)

    return(
        <div>
            <h1>{props.firstName},{props.lastName}</h1>
            <h2>age : {newAge}</h2>
            <h2>age : {props.hairColor}</h2>
            <button onClick={birth}>add year</button>


        </div>
    )
}
export default PersonCard 