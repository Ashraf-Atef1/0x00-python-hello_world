#!/usr/bin/python3
def no_c(my_string):
    while my_string.find("c") >= 0:
        str_list = [*my_string]
        del str_list[str_list.index("c")]
        my_string = "".join(str_list)
    while my_string.find("C") >= 0:
        str_list = [*my_string]
        del str_list[str_list.index("C")]
        my_string = "".join(str_list)
    return my_string
