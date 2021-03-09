"""Homework file for my students to have fun with some algorithms! """

def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    #Return the value 
    find_greatest_number = max(incoming_list)
    return find_greatest_number

def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    #Return the value
    find_least_number = min(incoming_list)
    return find_least_number
    
def add_list_numbers(incoming_list):
    """
    Required parameter incoming_list, should be a list.
    Add all the values together and return it.
    """
    #Return the value 
    total = sum(incoming_list)
    return total

def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    #Return the value
    longest_value_key = max(incoming_dict, key=len)
    return longest_value_key
