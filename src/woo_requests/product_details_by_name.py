import requests
from requests.auth import HTTPBasicAuth
import json
from bs4 import BeautifulSoup


def product_details_by_name(main_field):
    
    base_url = 'https://spider3d.co.il'
    consumer_key = 'ck_10860d370ddb79f39b4da3a765960cfd05842cfa'
    consumer_secret = 'cs_5265e43f6e72275fc510c86dee08ae81b08c8e97'
    # product_name = 'ּּ+PLAּ סילק מטאלי אדום Silk Red'
    product_name = main_field
    
    endpoint = f'{base_url}/wp-json/wc/v3/products'
    params = {
        'search': product_name,
        'per_page': 1 
    }
    
    response = requests.get(endpoint, auth=HTTPBasicAuth(consumer_key, consumer_secret), params=params)
    
    if response.status_code == 200:
    
        products = response.json()
        if products:
            # print(products[0])
            
                # Exanple: https://spider3d.co.il/wp-json/wc/v3/products?search=%D6%BC%D6%BC+PLA%D6%BC%20%D7%A1%D7%99%D7%9C%D7%A7%20%D7%9E%D7%98%D7%90%D7%9C%D7%99%20%D7%90%D7%93%D7%95%D7%9D%20Silk%20Red&consumer_key=ck_10860d370ddb79f39b4da3a765960cfd05842cfa&consumer_secret=cs_5265e43f6e72275fc510c86dee08ae81b08c8e97

            try:
                permalink = products[0]['permalink']
            except KeyError:
                permalink = '-'

            try:
                id = products[0]['id']
            except KeyError:
                id = '-'

            try:
                name = products[0]['name']
            except KeyError:
                name = '-'

            try:
                price = products[0]['price']
            except KeyError:
                price = '-'

            try:
                sku = products[0]['sku']
            except KeyError:
                sku = '-'

            try:
                image = products[0]['images'][0]['src']
            except (KeyError, IndexError):
                image = '-'

            try:
                description_html = products[0]['description']
                clean_desc = extract_text_from_html(description_html)
            except KeyError:
                description_html = '-'
                clean_desc = '-'

            
            return [permalink, id, name, clean_desc, price, image,sku ]
        else:
            print("Product not found.")
            return []
    else:
        print("Failed to retrieve products. Status code:", response.status_code)
        return []


def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    return soup.get_text(separator='\n', strip=True)