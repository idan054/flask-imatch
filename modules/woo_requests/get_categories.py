import os

import requests
from requests.auth import HTTPBasicAuth
import json
from bs4 import BeautifulSoup
from woocommerce import API


def get_woo_categories(web_field, cs_field, ck_field, ):
    base_url = web_field
    consumer_key = ck_field
    consumer_secret = cs_field

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

    errList = [

        {
            'id': 0,
            'name': '1. קטגוריות לא זוהו - נא לפנות אל האיש הטכני / מנהל האתר',
        },

        {
            'id': 1,
            'name': '2. קטגוריות לא זוהו - יש לוודא שהמפתח CS CK תקינים והמפתח משוייך למשתמש מנהל https://ibb.co/Y35cVRD',
        },

        {
            'id': 2,
            'name': '3. קטגוריות לא זוהו - יש לוודא שכתובת האתר הוזנה בצורה תקינה https://your-site.co.il',
        },

        {
            'id': 3,
            'name': '4. קטגוריות לא זוהו - ייתכן שהשרת / אתר שלך חוסם את הבקשה כאמצעי הגנה למניעת CORS',
        }
    ]

    try:
        endpoint = f'{base_url}/wp-json/wc/v3/products/categories?per_page=100&_fields=id,name'
        response = requests.get(endpoint, auth=HTTPBasicAuth(consumer_key, consumer_secret))

        if response.status_code == 200:
            categories = response.json()

            # file_path = os.path.join(os.getcwd(), 'categories.json')
            # Write the categories to a file
            # with open(file_path, mode='w') as file:
            #     json.dump(categories, file, ensure_ascii=False, indent=4)

            return response.json()

        return errList

    except:
        return errList
