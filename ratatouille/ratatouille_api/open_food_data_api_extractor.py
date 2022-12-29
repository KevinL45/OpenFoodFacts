import json
import functools

# KEYS_TO_EXTRACT = [
#     '_keywords',
#     # 'product_name_fr',
#     'nutriscore_data',
#     'ecoscore_data',
#     'ingredients_original_tags',
#     'image_url',
#     'stores_tags',
#     'teams_tags',
#     'ingredients_analysis',
#     # 'ingredients_text_fr'
# ]

MAP_EXTRACT_DATA_KEY_WITH_PRODUCT_KEY = {
    'name':'product_name_fr',
    'categories' : '_keywords',
    'nutriscore': 'nutriscore_data',
    'ecoscore' :'ecoscore_data',
    'ingredients' :'ingredients_original_tags',
    'link': 'image_url',
    'store' : 'stores_tags',
    # 'categories': 'teams_tags',
    'ingredients': 'ingredients_analysis',
}

def getFieldsToExtract():
    generated_chain = ""
    return functools.reduce(lambda chain, elem : chain + ","+elem, MAP_EXTRACT_DATA_KEY_WITH_PRODUCT_KEY.values())

# may be deprecated with diles URI paramter use
def extractData(open_data_food_api_product_data, nb_element_to_extract= 10):
    data_extracted = []
    if open_data_food_api_product_data != None and len(open_data_food_api_product_data) != 0:
        data= json.loads(open_data_food_api_product_data)
        data_products = data['products']
        for data_product in data_products[0:nb_element_to_extract]: 
            data_product_extracted = {}
            for key_to_extract in MAP_EXTRACT_DATA_KEY_WITH_PRODUCT_KEY.values():
                data_extracted_temp = data_product[key_to_extract]
                if data_extracted_temp != None:
                    data_product_extracted[key_to_extract] = data_extracted_temp
            data_extracted.append(data_product_extracted)
    return data_extracted
    
def mapDatasToProducts(product_datas):
        products_mapped = []
        if product_datas != None and len(product_datas) != 0:
            for product_data in product_datas:
                product_mapped_temp = mapDataToProduct(product_data)
                if product_mapped_temp != None:
                    products_mapped.append(product_mapped_temp)
        return products_mapped

def mapDataToProduct(product_data):
    product_mapped = None
    if product_data != None:
        product_mapped = {}
        for key in MAP_EXTRACT_DATA_KEY_WITH_PRODUCT_KEY.keys():
            product_mapped[key] = product_data[MAP_EXTRACT_DATA_KEY_WITH_PRODUCT_KEY[key]]
    return product_mapped
