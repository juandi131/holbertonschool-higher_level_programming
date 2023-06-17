#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best = 0
        str = [""]
        for elements in a_dictionary:
            if best < a_dictionary[elements]:
                best = a_dictionary[elements]
                str = elements
        return str
    else:
        return None
