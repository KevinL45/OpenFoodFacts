// import fetch from 'node-fetch';

export class RatatouilleApiClient {

    RATATOUILLE_API_URL = "http://localhost:8000/ratatouille_api"

    async searchProduct(productName)  {
       let SEARCH_PRODUCT_URL = `${this.RATATOUILLE_API_URL}/search/product/${productName}`

       return await fetch(SEARCH_PRODUCT_URL)
            .then(response =>  {
                if (response.ok) {
                    return response
                }
                throw new Error("Fail to find Product")
            }).then(response => {
                return response.json()
            })
    }

    async getProductsHomepage(size_page)  {
        let SEARCH_PRODUCT_URL = `${this.RATATOUILLE_API_URL}/home/products/${size_page}`
    
        return await fetch(SEARCH_PRODUCT_URL)
            .then(response =>  {
                if (response.ok) {
                    return response
                }
                throw new Error("Fail to find Products")
            }).then(response => {
                return response.json()
            })
        }

    async searchProductBarcode(barcode)  {
        let SEARCH_PRODUCT_CODE_URL = `${this.RATATOUILLE_API_URL}/search/product/code/${barcode}`
    
        return await fetch(SEARCH_PRODUCT_CODE_URL)
            .then(response =>  {
                if (response.ok) {
                    return response
                }
                throw new Error(`Fail to find Product with code ${barcode}`)
            }).then(response => {
                return response.json()
            })
        }

    async getMenus() {
        let MENU_URL = `${this.RATATOUILLE_API_URL}/menus/`

        return await fetch(MENU_URL)
             .then(response =>  {
                 if (response.ok) {
                     return response
                 }
                 throw new Error("Fail to find menu")
             }).then(response => {
                 return response.json()
             })
    }

}
