import React,{useState} from "react";
import Display from "./display";


const Form =()=>{

    const [users,setusers]=useState ([])


    const [firstName,setfirstName]=useState ("")
    const [lastName,setlastName]=useState ("")
    const [Email,setEmail]=useState ("")
    const [Password,setPassword]=useState ("")
    const [Confirmpass,setConfirmpass]=useState ("")


    const newuser=(e) =>{
        e.preventDefault()
        const newUser = { firstName,lastName,Email,Password,Confirmpass}
        setusers([...users,newUser])
        
    }



    return(
        <div>
            <form onSubmit={(e)=> newuser(e)}>
                <div>
                    <label >First Name</label>
                    <input type="text" onChange={e =>setfirstName(e.target.value)}  />
                </div>
                <div>
                    <label >Last Name</label>
                    <input type="text" onChange={e =>setlastName(e.target.value)}  />
                </div>
                <div>
                    <label >Email</label>
                    <input type="text" onChange={e =>setEmail(e.target.value)}  />
                </div>
                <div>
                    <label >Password</label>
                    <input type="text" onChange={e =>setPassword(e.target.value)}  />
                </div>
                <div>
                    <label >Confirm Your Password</label>
                    <input type="text" onChange={e =>setConfirmpass(e.target.value)}  />
                </div>
                <input type="submit" value='add' />
            </form>
            {users.map((user,idx)=> <Display key={idx} user={user}/>)}

        </div>
    )
}

export default Form