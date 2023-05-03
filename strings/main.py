# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# Name scoring players
player_scored1 = "Ruud Gullit"
player_scored2 = "Marco van Basten"

# Add scoring minutes
goal_0 = 32
goal_1 = 54
goal_0_str = str(goal_0)
goal_1_str = str(goal_1)

# Scoring minute per player
scorers = player_scored1 + " " + goal_0_str + ", " + player_scored2 + " " + goal_1_str

report = player_scored1 + " scored in the " + goal_0_str + "nd minute\n" + player_scored2 + " scored in the " + goal_1_str + "th minute"
print(report)

# Slicing and find to isolate and store the player's first name.
player = "Ronald Koeman"
first_name = player[:player.find(" ")]

# Find, slicing and len to isolate and store the length of last name.
# last_name_len = len(player[(player.find(" ")+1):]) = in 1 sentence. The following is clearer:
last_name = player[player.find(" ")+1:]
last_name_len = len(last_name)

# Shortening name (R. Koeman)
name_short = first_name[0] + ". " + last_name

# Make chants
x = len(first_name) - 1
chant = ((first_name + "! ") * x + first_name + "!")
print(chant)

# Check if last character isn't a space
good_chant = chant[-1] != " "
print(good_chant)