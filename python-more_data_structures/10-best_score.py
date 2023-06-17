#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    values = list(a_dictionary.values())
    b = len(values) - 1
    for a in range(b):
        best = values[a]
        if values[a] < values[a + 1]:
            best = values[a + 1]
    for key in a_dictionary:
        if a_dictionary[key] == best:
            return(key)
