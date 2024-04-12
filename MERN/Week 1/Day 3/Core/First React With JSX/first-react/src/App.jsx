import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <div>
       <h1>Hello Dojo</h1>
       <ul>
        <h2>to do list</h2>
        <li>learn</li>
        <li>climb</li>
        <li>run</li>
        <li>feed</li>
       </ul>
      </div>
    </>
  )
}

export default App
