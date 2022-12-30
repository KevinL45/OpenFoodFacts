import { useState, useEffect } from 'react';
import { useLayoutEffect } from 'react';
import Button from 'react-bootstrap/Button';
import Card from 'react-bootstrap/Card';
import { RatatouilleApiClient } from '../services/RatatouilleApiClient';
import {Routes, Route, useNavigate} from 'react-router-dom';
import Chip from '@material-ui/core/Chip';

function Home() {

  const navigate = useNavigate();
   
  const [products, setProducts] = useState()
  const [menus, setMenus] = useState()
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
      // await ratatouilleApiClient.getMenus().then(data => {
      //   console.log(data)
      //   // setProducts(data_parsed)
      //   setMenus(data)
      //   setShow(true)

      // })
    }
    fetchData()
  }, [])

  function onClickDetail(product_id)  {
    navigate(`/detail/${product_id}`);
  }

//   { (menus != undefined && show) ?
//     <div>
//       {
//         menus.map((menu, index) => {
//           return (
//             <Card key={index} style={{ width: '18rem' }}>
//               <Card.Body>  
//                 <Card.Title>{menu.name}</Card.Title>
//                 {/* <img src={product.image_url} style={{ maxWidth: '200px', maxHeight: '200px'}}></img> */}
//                 <Card.Text>
//                   Some quick example text to build on the card title and make up the
//                   bulk of the card's content.
//                 </Card.Text>
//                 {/* {menu.dishes.split(',').map(elem => <Chip label={elem} variant="outlined" />)} */}
//                 <Button variant="primary" onClick={() => onClickDetail(menu._id)}>Detail</Button>
//               </Card.Body>
//             </Card>
//           )
//         })
//       }
//     </div>
//     : <div>
//         <span>Menus not found</span>
//       </div>
// } 

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
                      {product.categories.split(',').map(elem => <Chip label={elem} variant="outlined" />)}
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
