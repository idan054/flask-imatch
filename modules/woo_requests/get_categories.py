import os

import requests
from requests.auth import HTTPBasicAuth
import json
from bs4 import BeautifulSoup
from woocommerce import API


def get_woo_categories():
    base_url = 'https://spider3d.co.il'
    consumer_key = 'ck_3cd2f0123e4f2c75762cb7cba116c60a333ccfd4'
    consumer_secret = 'cs_5d42c2d29dd618c948edd57d3b9b8b48353f38b9'
    # product_name = 'חומר גלם'

    # file_path = 'settings.txt'
    # config = {}
    # with open(file_path, 'r') as file:
    #     for line in file:
    #         key, value = line.strip().split('=')
    #         config[key.strip()] = value.strip()
    #
    # base_url = config.get('base_url', '')
    # consumer_key = config.get('consumer_key', '')
    # consumer_secret = config.get('consumer_secret', '')

    # base_url = 'https://avners.co.il'
    # consumer_key = 'ck_40277bba2e0d959fb2ec3aed808e01db800f4c1f'
    # consumer_secret = 'cs_ffefd520797cef75c3a9c5cea3dd477c2fa585bf'

    endpoint = f'{base_url}/wp-json/wc/v3/products/categories?per_page=100&_fields=id,name'
    response = requests.get(endpoint, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    # if response.status_code == 200:
    # categories = response.json()

    # file_path = os.path.join(os.getcwd(), 'categories.json')
    # Write the categories to a file
    # with open(file_path, mode='w') as file:
    #     json.dump(categories, file, ensure_ascii=False, indent=4)

    return {"status_code": str(response.status_code), "content": str(response.content)}

    # return None
