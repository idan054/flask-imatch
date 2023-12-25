import os
from flask import render_template, request, json


def save_config_locally(web_field, ck_field, cs_field):
    data = {
        "base_url": str(web_field),
        "consumer_key": str(ck_field),
        "consumer_secret": str(cs_field)
    }
    file_path = os.path.join(os.getcwd(), 'static/data', 'config.json')
    with open(file_path, mode='w') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def try_get_local_config():
    try:
        with open(os.path.join(os.getcwd(), 'static/data', 'config.json'), mode='r') as my_file:
            config = json.load(my_file)
    except Exception as e:
        print(e)
        config = {
            "base_url": "",
            "consumer_key": "",
            "consumer_secret": ""
        }
    return config
