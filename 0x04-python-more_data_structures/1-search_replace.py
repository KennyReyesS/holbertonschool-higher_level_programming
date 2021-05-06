#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if my_list is None:
        return None
    else:
        new_list = my_list.copy()
        for i in new_list:
            new_list[search - 1] = replace
        return(new_list)
