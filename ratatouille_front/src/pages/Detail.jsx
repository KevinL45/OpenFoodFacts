import { useParams } from "react-router-dom";
import { useState, useLayoutEffect } from "react";
import Card from 'react-bootstrap/Card';
import { RatatouilleApiClient } from "../services/RatatouilleApiClient";


function Detail() {

    const[product, setProduct] = useState()
    let {product_id} = useParams();
    let ratatouilleApiClient = new RatatouilleApiClient()
    
    useLayoutEffect(() => {
      async function fetchData() {  
        if (product_id != undefined) {
          await ratatouilleApiClient.searchProductBarcode(product_id)
          .then(data => {
            console.log(data[0])
            setProduct(data[0]) 
            console.log(product)
          })
        }
      }
      fetchData()
    }, [])

    // const {product_id} = route.params;



    return (
      <div className="App">
          { product != undefined ?
          <div>
            <Card style={{ width: '38rem' }}>
            <Card.Body>  
              <Card.Title>{product.name}</Card.Title>
              <img src={product.link} style={{ maxWidth: '200px', maxHeight: '200px'}}></img>
              <Card.Text>
                  { product.nutriscore != undefined && product.nutriscore.size != 0 ?
                      <span>Nutriscores : {Object.keys(product.nutriscore).map(key => {
                        return (<section>
                                  <span>{key} : {product.nutriscore[key]}</span>
                                  <br/>
                              </section>)
                      })}</span>
                    :
                    <span>Nutriscore not Found</span>
                  }
              </Card.Text>
              <span>categories : {product.categories.reduce((chain, elem) => chain + ", " + elem)}</span>
              <br/><br/>
              <span>magasins : {product.store.reduce((chain, elem) => chain + ", " + elem)}</span>
              <br/><br/>
            </Card.Body>
          </Card>
          </div>
          :
          <div>
            <span>No product found yet</span>
          </div>

        }
      </div>
    );
  }
  
  export default Detail;
  