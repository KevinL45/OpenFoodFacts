import {Routes, Route} from 'react-router-dom';
import Home from "./pages/Home"
import Products from "./pages/Products"
import Detail from "./pages/Detail"
import Auth from "./pages/Auth"
import Navbar from "./components/Navbar"

function App() {
  return (
    <div className="App">
      <Navbar/>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/auth' element={<Auth/>}/>
        <Route path='/products' element={<Products/>}/>
        <Route path='/detail' element={<Detail/>}/>
      </Routes>
    </div>
  );
}

export default App;
