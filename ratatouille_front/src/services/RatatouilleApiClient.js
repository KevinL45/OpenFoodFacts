// import fetch from 'node-fetch';

export class RatatouilleApiClient {

    async searchProduct(productName)  {
    let SEARCH_PRODUCT_URL = `http://localhost:8000/ratatouille_api/search/product/${productName}`

       return await fetch(SEARCH_PRODUCT_URL)
            .then(response =>  {
                if (response.ok) {
                    return response
                }
                throw new Error("Fail to find Productd")
            }).then(response => {
                return response.json()
            })
    }
}
