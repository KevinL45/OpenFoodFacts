import requests
from django.conf import settings

class OpenFoodApi():
    # SEARCH_PRODUCT_URI ='https://fr.openfoodfacts.org/cgi/search.pl?search_terms=Danette&search_simple=1&action=process&json=True'
    SEARCH_PRODUCT_URI ='https://fr.openfoodfacts.org/cgi/search.pl?search_simple=1&action=process&json=true'

    def findProduct(self, product_name): 
        product_data = None
        if product_name != None and len(product_name) != 0:
            response = requests.get(self.SEARCH_PRODUCT_URI, {'search_terms': product_name})
            if response.status_code == 200:
                product_data = response.text
            else:
                product_data = None
        return product_data
    
