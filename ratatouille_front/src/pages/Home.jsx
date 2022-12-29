import { useState, useEffect } from 'react';
import { useLayoutEffect } from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { RatatouilleApiClient } from '../services/RatatouilleApiClient';
import {Routes, Route, useNavigate} from 'react-router-dom';

function Home() {

  const navigate = useNavigate();
   
  const [products, setProducts] = useState()
  let [show, setShow] = useState(false)

  let ratatouilleApiClient = new RatatouilleApiClient()

  useLayoutEffect(() => {
    async function fetchData() {
      await ratatouilleApiClient.getProductsHomepage(9).then(data => {
        let data_parsed = JSON.parse(data)
        console.log(data_parsed['products'])
        setProducts(data_parsed['products'])
        setShow(true)
      })
    }
    fetchData()
  }, [])

  function onClickDetail(product_id)  {
    navigate(`/detail/${product_id}`);
  }

  return (
    <div className="App">

      { (products != undefined && show) ?
          <div>
            {
              products.map((product, index) => {
                return (
                  <Card key={index} style={{ width: '18rem' }}>
                    <Card.Body>  
                      <Card.Title>{product.product_name_fr}</Card.Title>
                      <img src={product.image_url} style={{ maxWidth: '200px', maxHeight: '200px'}}></img>
                      <Card.Text>
                        Some quick example text to build on the card title and make up the
                        bulk of the card's content.
                      </Card.Text>
                      <span>{product.categories}</span>
                      <Button variant="primary" onClick={() => onClickDetail(product._id)}>Detail</Button>
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

export default Home;
