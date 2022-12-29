import { useEffect } from 'react';
import { useState } from 'react';
import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import NavDropdown from 'react-bootstrap/NavDropdown';
import { RatatouilleApiClient } from '../services/RatatouilleApiClient';

function BasicExample() {

const[message, setMessage] = useState("")
const[product, setProducts] = useState()
let ratatouilleApiClient = new RatatouilleApiClient()

// useEffect(() => {
//   ratatouilleApiClient = new RatatouilleApiClient()
// }, []) 

async function search() {
  console.log("search "  + message)
  if (ratatouilleApiClient != undefined) {
    let products_temp = await ratatouilleApiClient.searchProduct(message)
    setProducts(products_temp)
    console.log(products_temp)
  }
}

function onChange(event) {
  let value = event.target.value
  setMessage(value)
}

  return (
    <Navbar bg="light" expand="lg">
      <Container>
        <Navbar.Brand href="#home">OpenFoodFacts</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link href="/">Accueil</Nav.Link>
            <Nav.Link href="/products">Produits</Nav.Link>
            <Nav.Link href="/register">Inscription</Nav.Link>
            <Nav.Link href="/auth">Connexion</Nav.Link>
          </Nav>
        </Navbar.Collapse>
        <Container>
          <input type="search" id="search" autoComplete="off" onChange={onChange}/>
          <button onClick={search} >Search</button>
        </Container>
      </Container>
    </Navbar>
  );
}


export default BasicExample;