#!/usr/bin/python3
""" student stent """


class Student:
    """ student dent """
    def __init__(self, first_name, last_name, age):
        """ init init """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ to json """
        if type(attrs) == list:
            new_dic = {}
            for tt in self.__dict__:
                if tt in attrs:
                    new_dic[tt] = self.__dict__.get(att)
            return new_dic
        else:
            return self.__dict__

    def reload_from_json(self, json):
        """ reload from json """
        self.__dict__.update(json)