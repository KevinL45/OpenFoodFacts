import { useParams } from "react-router-dom";

function Detail() {

    // const {product_id} = route.params;
    let {product_id} = useParams();

    return (
      <div className="App">
        <span>{product_id}</span>
      </div>
    );
  }
  
  export default Detail;
  