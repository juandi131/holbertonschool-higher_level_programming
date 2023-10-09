#!/usr/bin/python3
""" load n """
import json


def load_from_json_file(filename):
    """ lo fr sonile """
    with open(filename) as f:
        return json.load(f)
    