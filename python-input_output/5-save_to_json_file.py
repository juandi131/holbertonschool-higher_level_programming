#!/usr/bin/python3
""" sa to json """
import json


def save_to_json_file(my_obj, filename):
    """ savon """
    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
        
