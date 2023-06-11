#!/usr/bin/python3
def no_c(my_string):
    char_list = list(my_string) 
    for i in range(len(my_string)):
        if my_string[i] == 'C' or my_string[i] == 'c':
            my_string[i] == ""
        new_string = "".join(char_list)
    return my_string
