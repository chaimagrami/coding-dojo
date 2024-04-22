import logo from './logo.svg';
import './App.css';
import { Route, Routes,Link } from 'react-router-dom';
import People from './components/People'
import Planet from './components/Planets'
import Error from './components/Error'
import Form from './components/Form'


function App() {
  return (
    <div className="App">
        <h2>Luke APIwalker</h2>
        <Form/>
      <Routes>
        <Route path='/error' element={<Error/>}/>
        <Route path='/:choice/:id' element={<People/>} />
        <Route path='/:id' element={<Planet/>} />
        <Route path='/*' element={<Error/>} />
      </Routes>
    </div>
  );
}

export default App;
