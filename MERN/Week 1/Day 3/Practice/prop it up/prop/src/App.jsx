import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import PersonCard from './components/cards'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
    <PersonCard firstName={"chaima"} lastName={"grami"} age={"22"} hairColor={"black"}/>
    <PersonCard firstName={"chaima"} lastName={"grami"} age={"22"} hairColor={"black"}/>
    <PersonCard firstName={"chaima"} lastName={"grami"} age={"22"} hairColor={"black"}/>
    <PersonCard firstName={"n3oucha"} lastName={"atiaoui"} age={"22"} hairColor={"brown"}/>
    </>
  )
}

export default App
