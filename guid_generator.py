import random
import string
import sys

def list_to_string(s): 
    """Takes a list as argument"""
    str1 = ""  
    for ele in s: 
        str1 += str(ele)  
    return str1

def guid_part_generator(limit):
    """Generates part of a guid, length based on argument limit"""
    x = 0
    random_numbers_list = []
    random_letters_list = []
    lower_upper_alphabet = string.ascii_letters
    while x < limit:
        number = random.randint(0,9)
        random_numbers_list.append(number)
        random_letter = random.choice(lower_upper_alphabet)
        letter = random_letter.lower()
        random_letters_list.append(letter)    
        x+=1
    random.shuffle(random_numbers_list)
    guid_list = random_numbers_list + random_letters_list
    random.shuffle(guid_list)
    guid_part = list_to_string(guid_list)
    return(guid_part)

def guid_generator(input_list, separator):
    """Generates guid consisting of parts in the input_list and separated by what you input in the separator argument"""
    start_guid = ""
    for i in input_list:
        part = guid_part_generator(limit = i)
        start_guid += part
        start_guid += separator
    guid = start_guid[:-1]
    return(guid)

firstarg = [4,2,2,2,6]
secondarg = "-"

home_made_guid = guid_generator(input_list = firstarg, separator = secondarg)
print(home_made_guid)

# firstarg=sys.argv[1]
# secondarg=sys.argv[2]
# print(firstarg)
# print(secondarg)