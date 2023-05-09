# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line
def alphabetical_order(film_names):
    return sorted(film_names)

def won_golden_globe(film_name):
    awards = ['jaws', 'star wars: episode IV - a new hope', 'e.t. the extra-terrestrial', 'memoirs of a geisha']
    
    if film_name.lower() in awards:
        return True
    else:
        return False


def remove_toto_albums(check_albums):
    toto_albums = ['Fahrenheit', 'The Seventh One', 'Toto XX', 'Falling in Between', 'Toto XIV', 'Old Is New']

    for album in toto_albums:
        if album in check_albums:
            check_albums.remove(album)
    
    return check_albums
