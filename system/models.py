from django.db import models
import os
import json


class Model:
    def get_json_data(self):
        file_path = '\\terminal_automation\\automation\\reports\\history.json'
        all_path = os.path.dirname(os.getcwd()) + file_path
        final_path = all_path.replace('\\', '/')
        with open(final_path,'r',encoding = 'utf-8') as fp:
            data = json.load(fp)
        return data

