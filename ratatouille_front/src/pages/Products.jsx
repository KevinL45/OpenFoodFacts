import { useEffect, useState } from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { useNavigate } from 'react-router-dom';
import Chip from '@material-ui/core/Chip';

function Products({productsSearch}) {

  const navigate = useNavigate();

  const[products, setProducts] = useState()

  useEffect(() =>  {
    setProducts(...[productsSearch])
    console.log(products)
  }, productsSearch)

  function onClickDetail(product_id)  {
    navigate(`/detail/${product_id}`);
  }
  
  return (
    <div className="App">
            {/* <Card style={{ width: '18rem' }}>
      <Card.Img variant="top" src="holder.js/100px180" />
      <Card.Body>  
        <Card.Title>Card Title</Card.Title>
        <Card.Text>
          Some quick example text to build on the card title and make up the
          bulk of the card's content.
        </Card.Text>
        <Button variant="primary">Go somewhere</Button>
      </Card.Body>
    </Card> */}

    { (products != undefined) ?
          <div>
            {
              products.map((product, index) => {
                return (
                  <Card key={index} style={{ width: '18rem' }}>
                    <Card.Body>  
                      <Card.Title>{product.name}</Card.Title>
                      <img src={product.link} style={{ maxWidth: '200px', maxHeight: '200px'}}></img>
                      <Card.Text>
                        <br/>
                        <span> energy {product.nutriscore['energy'] || "not found"} </span>
                        <br/>
                        <span> nutriscore grade : {product.nutriscore['grade'] || "not found"}</span>
                        <br/>
                        <span> ecoscore : {product.ecoscore['grade'] || "not found"}</span>
                      </Card.Text>
                      {product.categories.map(elem => <Chip label={elem} variant="outlined" />)}
                      
                      {/* <span>{product.categories.reduce((chain, elem) => chain + ", " + elem)}</span> */}
                      <Button variant="primary" onClick={() => onClickDetail(product.barcode)}>Detail</Button>
                    </Card.Body>
                  </Card>
                )
              })
            }
          </div>
          : <div>
              <span>Products not found</span>
            </div>
      }
    </div>
  );
}

export default Products;
