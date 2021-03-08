"""Homework file for my students to have fun with some algorithms! """


def find_greatest_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the largest number in the list.
    """

#Create a list
GreatestN=[1,2,3,4,5,6,7,8]

#Find the greatest number in the list 
find_greatest_number = max(GreatestN)
print("The greatest number is:", find_greatest_number)


def find_least_number(incoming_list):
    """
    Required parameter, incoming_list, should be a list.
    Find the smallest/least number in the list.
    """

    #Create a List
SmallestN=[1,2,3,4,5,6,7,8]

    #Find the smallest number in the list
find_least_number = min(SmallestN)
print("The smallest number is:", find_least_number)
    

def add_list_numbers(incoming_list):
    """
    Required parameter incoming_list, should be a list.
    Add all the values together and return it.
    """
    #Create a List 
SumOFList=[1,2,3,4]

    #Find the sum of the numbers in the list 
total = sum(SumOFList)
print("The sum of this list is:", total)

def longest_value_key(incoming_dict):
    """
    Required parameter, incoming_dict, should be a dict.
    Find the KEY that has a value with the highest length, use the len() function
    """
    #Create list of keys 
longest_value_key = ({"dog": "cat", "a": "asdfasdfasdfasdfasdf"})

    #Find the longest value key
longest_value_key = max(longest_value_key, key=len)
print(longest_value_key)
