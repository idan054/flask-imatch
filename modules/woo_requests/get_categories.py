import os

import requests
from requests.auth import HTTPBasicAuth
import json
from bs4 import BeautifulSoup
from woocommerce import API


def get_woo_categories():
    # base_url = 'https://spider3d.co.il'
    # consumer_key = 'ck_10860d370ddb79f39b4da3a765960cfd05842cfa'
    # consumer_secret = 'cs_5265e43f6e72275fc510c86dee08ae81b08c8e97'
    # product_name = 'חומר גלם'

    file_path = 'settings.txt'
    config = {}
    with open(file_path, 'r') as file:
        for line in file:
            key, value = line.strip().split('=')
            config[key.strip()] = value.strip()

    base_url = config.get('base_url', '')
    consumer_key = config.get('consumer_key', '')
    consumer_secret = config.get('consumer_secret', '')

    endpoint = f'{base_url}/wp-json/wc/v3/products/categories?per_page=100&_fields=id,name'
    response = requests.get(endpoint, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    if response.status_code == 200:
        categories = response.json()

        file_path = os.path.join(os.getcwd(), 'categories.json')

        # Write the categories to a file
        with open(file_path, mode='w') as file:
            json.dump(categories, file, ensure_ascii=False, indent=4)

        return categories

    return None
