import os

import pandas as pd
from flask import render_template, request
from modules.addRow import addRows
from modules.woo_requests.get_categories import get_woo_categories
from modules.woo_requests.product_details_by_name import product_details_by_name
from modules.woo_requests.products_from_category import get_products_from_category


def configure_routes(app):
    @app.route("/")
    def index():
        # hello = modules.hello()
        # return render_template("sample_index.html", hello=hello, content=content)
        return render_template("index.html")

    @app.route('/success', methods=['POST', 'GET'])
    def success():
        if request.method == 'POST':
            data = request.get_json()
            main_field = data['main_field']
            selectedRadioValue = data['selectedRadioValue']
            print(main_field)
            print("selectedRadioValue")
            print(selectedRadioValue)

            if selectedRadioValue == 0:
                product_details_by_name(main_field)
            else:
                get_products_from_category(main_field, selectedRadioValue)

        return render_template('success.html')

    @app.route('/woo_api')
    def woo_api():
        categories = get_woo_categories()
        print("categories")
        print(categories)
        return categories

    @app.route('/get_category', methods=['POST', 'GET'], )
    def get_category():
        if request.method == 'POST':
            print("START get_woo_categories")

        # Save locally
        try:
            with open(os.path.join(os.getcwd(), '', 'categories.json'), mode='r') as my_file:
                json_categories = my_file.read()
                return json_categories

        except:
            # data = request.get_json()
            # main_field = data['main_field']
            categories = get_woo_categories()
            print("categories")
            print(categories)
            return categories
