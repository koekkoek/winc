from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

def shortest_names(country_list):
    x = 20
    new_list = []

    for country in country_list:
        length = len(country)
        if length < x:
            x = length

    for country in country_list:
        if len(country) == x:
            new_list.append(country)
    
    return new_list


def most_vowels(country_list):
    vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    count = 0
    new_list = []

    for country in country_list:
        count_word = 0

        for letter in country:
            if letter in vowels:
                count_word += 1
        
        new_list.append([count_word, country])

    new_list.sort()
    new_list[-1] = new_list[-1][1]
    new_list[-2] = new_list[-2][1]
    new_list[-3] = new_list[-3][1]

    return new_list[-3:]

def alphabet_set(country_list):

    print(country_list)
    alphabet = list('abcdefghijklmnopqrstuvwxyz')
    new_list = []

    for country in country_list:
        for char in country:
            if char in alphabet and len(new_list) < 14:
                new_list.append(country)
                print(alphabet)

                for char in country:
                    if char in alphabet:
                        alphabet.remove(char)
                
                print(alphabet)

    print(new_list)
    return new_list

# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()

    """ Write the calls to your functions here. """
