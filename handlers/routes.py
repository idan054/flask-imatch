import os
from flask import render_template, request
from modules.addRow import addRow
from modules.woo_requests.product_details_by_name import product_details_by_name


def configure_routes(app):
    @app.route("/")
    def index():
        # hello = modules.hello()
        # return render_template("sample_index.html", hello=hello, content=content)
        return render_template("index.html")

    @app.route('/success', methods=['POST', 'GET'])
    def success():
        if request.method == 'POST':
            main_field = request.form['main_field']
            print(main_field)
            data = product_details_by_name(main_field)
            addRow(data)
        return render_template('success.html')

    @app.route('/api')
    def api():
        with open(
            os.path.join(os.getcwd(), 'static/data', 'data.json'), mode='r'
        ) as my_file:
            text = my_file.read()
            return text

   

    @app.route('/woo_api')
    def woo_api():
        data = product_details_by_name("כחול")
        return data
#



