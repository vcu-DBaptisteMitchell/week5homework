"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """
    print("The greatest number is:", max(find_greatest_number))



def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """
    print("The smallest number is:", (min(find_least_number))
    )


def add_list_numbers(incoming_list):
    """
    Required parameter incoming_list, should be a list.
    Add all the values together and return it.
    """
    total = sum(add_list_numbers)
    print("The sume of this list is:", total)

def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    longest_value_key = max(longest_value_key, key=len)
    print(longest_value_key)
