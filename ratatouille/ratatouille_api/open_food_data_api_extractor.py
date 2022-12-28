import json

KEYS_TO_EXTRACT = [
    '_keywords',
    # 'product_name_fr',
    'nutriscore_data',
    'ecoscore_data',
    'ingredients_original_tags',
    'image_url',
    'stores_tags',
    'teams_tags',
    'ingredients_analysis',
    # 'ingredients_text_fr'
]

def extractData(open_data_food_api_product_data):
    data_extracted = []
    if open_data_food_api_product_data != None and len(open_data_food_api_product_data) != 0:
        data= json.loads(open_data_food_api_product_data)
        data_products = data['products']
        for data_product in data_products[0:10]: 
            data_product_extracted = {}
            for key_to_extract in KEYS_TO_EXTRACT:
                data_extracted_temp = data_product[key_to_extract]
                if data_extracted_temp != None:
                    data_product_extracted[key_to_extract] = data_extracted_temp
            data_extracted.append(data_product_extracted)
    return data_extracted
