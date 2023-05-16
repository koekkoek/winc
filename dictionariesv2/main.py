# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line


def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    # Make a new passport
    passport = {
        'name': name,
        'date_of_birth': date_of_birth,
        'place_of_birth': place_of_birth,
        'height': height,
        'nationality': nationality,
        }

    return passport


def add_stamp(passport, country):
    # Checking for 'stamps'-key in passport
    # Checking for country-value in passport
    if 'stamps' not in passport.keys() and country not in passport['nationality']:
        passport['stamps'] = country
    # Checking for 'stamps-key in passport
    # Check if country isn't nationality
    # Check if country isn't already a stamp
    elif 'stamps' in passport.keys() and country not in passport['nationality'] and country not in passport.get('stamps'):
        # Make a temporary list. Adding the country to it. Overwrite list in 'stamps'-key with new list
        tmp_list = [passport.values()]
        tmp_list.append(country)
        passport['stamps'] = tmp_list

    return passport


def add_biometric_data(passport, biometric_type, biometric_data, date):
    # Isn't biometric a key? Make it!
    if 'biometric' not in passport.keys():
        passport['biometric'] = {}
    # Isn't bio_type a key in biometric? Make it! and add data & bio_data in a dict
    if biometric_type not in passport['biometric']:
        passport['biometric'][biometric_type] = {'date': date, 'value': biometric_data}
    # Is bio_type already in biometric? Add date & bio_data in a dict
    elif biometric_type in passport['biometric']:
        passport['biometric'][biometric_type] = {'date': date, 'value': biometric_data}
    return passport


countries = get_countries()
country = countries[1]
passport1 = create_passport('Henk', '1980-02-13', 'Bodegraven', 1.78, country)
print(passport1)
