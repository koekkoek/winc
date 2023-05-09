# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_the_day, cow_milking_status, location_of_the_cows, season, slurry_tank, grass_status):

    #take cows to cowshed
    if (time_of_the_day == 'night' and location_of_the_cows == 'pasture') or (weather == 'rainy' and location_of_the_cows == 'pasture'):
        return 'take cows to cowshed'
    
    #milk cows
    elif cow_milking_status:
        if location_of_the_cows == 'cowshed':
            return 'milk cows'
        elif location_of_the_cows == 'pasture':
            return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'
    
    #fertilize pasture
    elif slurry_tank and (weather == 'rainy' or weather == 'neutral'):
        if location_of_the_cows == 'cowshed':
            return 'fertilize pasture'
        elif location_of_the_cows == 'pasture':
            return 'take cows to cowshed\nfertilize pasture\ntake cows back to pasture'

    #mow grass
    elif grass_status and season == 'spring' and weather == 'sunny':
        if location_of_the_cows == 'cowshed':
            return 'mow grass'
        elif location_of_the_cows == 'pasture':
            return 'take cows to cowshed\nmow grass\ntake cows back to pasture'
    
    #wait
    else:
        return 'wait'


#farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)