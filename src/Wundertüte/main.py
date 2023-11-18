# in main.py
from userinputs import UserInput
from textcontrol import textcontrol

# Definition of variables
inputs = UserInput.ask_all()
dice_games_left = inputs[1]
card_games_left = inputs[2]
skill_games_left = inputs[3]
line = 0
id = 0
missed = []

# Create the framework
textcontrol.create_framework(inputs[0])

# Distribute dice games
for dice_game in range(1, dice_games_left + 1):
    if line == inputs[0]:
        line = 1
    else:
        line += 1

    textcontrol.add_data(line, "Dice Game", id)
    id += 1

# Distribute card games
for card_game in range(1, card_games_left + 1):
    if line == inputs[0]:
        line = 1
    else:
        line += 1

    textcontrol.add_data(line, "Card Game", id)
    id += 1

# Distribute skill games
for skill_game in range(1, skill_games_left + 1):
    if line == inputs[0]:
        line = 1
    else:
        line += 1

    textcontrol.add_data(line, "Skill Game", id)
    id += 1

# Add placeholders and add to the list
if line != inputs[0]:
    for i in range(line + 1, inputs[0] + 1):
        textcontrol.add_data(i, "missed", id)
        missed.append(id)
        id += 1
