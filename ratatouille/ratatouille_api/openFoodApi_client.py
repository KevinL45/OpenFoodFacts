import requests
from django.conf import settings
from ratatouille_api.open_food_data_api_extractor import extractData, mapDatasToProducts, getFieldsToExtract


class OpenFoodApi():
    # SEARCH_PRODUCT_URI ='https://fr.openfoodfacts.org/cgi/search.pl?search_terms=Danette&search_simple=1&action=process&json=True'
    SEARCH_PRODUCT_URI ='https://fr.openfoodfacts.org/cgi/search.pl?search_simple=1&action=process&sort_by=unique_scans_n&json=true'
    SEARCH_PRODUCT_URI_BY_POPULARITY = 'https://fr.openfoodfacts.org/?sort_by=popularity&json=true'
    SERACH_PRODUCT_URI_BY_BARCODE = 'https://fr.openfoodfacts.org/api/v2/search?&json=true'

    def findProduct(self, product_name): 
        products_data = None
        if product_name != None and len(product_name) != 0:
            fields_to_extract = getFieldsToExtract()
            # response = requests.get(self.SEARCH_PRODUCT_URI, {'search_terms': product_name, 'fields': fields_to_extract})
            response = requests.get(self.SEARCH_PRODUCT_URI, {'search_terms': product_name, 'page_size' :10})
            if response.status_code == 200:
                datas = extractData(response.text)
                products_data = mapDatasToProducts(datas)
            else:
                products_data = None
        return products_data
  
    def getProductByPopularity(self, page_size):
        products_data = None
        response = requests.get(self.SEARCH_PRODUCT_URI_BY_POPULARITY, {'page_size': page_size, 'fields': '_id,image_url,categories,product_name_fr'})
        if response.status_code == 200:
            products_data = response.text
            # products_data = extractData(response.text, page_size)
            # products_data = mapDatasToProducts(datas)
        else:
            products_data = None
        return products_data

    def getProductByBarcode(self, barcode):
        products_data = None
        response = requests.get(self.SEARCH_PRODUCT_URI_BY_POPULARITY, {'code': barcode})
        if response.status_code == 200:
            datas = extractData(response.text, 1)
            products_data = mapDatasToProducts(datas)
        else:
            products_data = None
        return products_data