import {Routes, Route} from 'react-router-dom';
import Home from "./pages/Home"
import Products from "./pages/Products"
import Detail from "./pages/Detail"
import Auth from "./pages/Auth"
import Register from './pages/Register';
import Navbar from "./components/Navbar"
import 'bootstrap/dist/css/bootstrap.min.css';
import { useState } from 'react';


function App() {

  const[products_search, setProductsSearch] = useState()

  function onSearchAction(search_result) {
    console.log(search_result)
    setProductsSearch(search_result)
  }

  return (
    <div className="App">
      <Navbar onSearchValue={onSearchAction}/>
      <Routes>
        <Route path='/' element={<Home/>}/>
        <Route path='/auth' element={<Auth/>}/>
        <Route path='/register' element={<Register/>}/>
        <Route path='/products' element={<Products productsSearch={products_search}/>}/>
        <Route path='/detail/:product_id' element={<Detail/>}/>
      </Routes>
    </div>
  );
}

export default App;
