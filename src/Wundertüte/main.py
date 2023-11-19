# in main.py
from userinputs import UserInput
from textcontrol import TextControl
from result import Result
print("All work is copyrighted by GNU GENERAL PUBLIC LICENSE. View the License (in main directory) for more information.")
# Definition of variables
inputs = UserInput.ask_all()
dice_games_left = inputs[1]
card_games_left = inputs[2]
skill_games_left = inputs[3]
line = 0
id = 0
missed = []

print("\033[93mStarted. Please wait...")
print("Press CTRL+C to cancel\033[0m")
# Create the framework
TextControl.create_framework(inputs[0])

# Distribute dice games
for dice_game in range(1, dice_games_left + 1):
    if line == inputs[0]:
        line = 1
    else:
        line += 1

    TextControl.add_data(line, "Dice Game", id)
    id += 1

# Distribute card games
for card_game in range(1, card_games_left + 1):
    if line == inputs[0]:
        line = 1
    else:
        line += 1

    TextControl.add_data(line, "Card Game", id)
    id += 1

# Distribute skill games
for skill_game in range(1, skill_games_left + 1):
    if line == inputs[0]:
        line = 1
    else:
        line += 1

    TextControl.add_data(line, "Skill Game", id)
    id += 1

# Add placeholders and add to the list
if line != inputs[0]:
    for i in range(line + 1, inputs[0] + 1):
        TextControl.add_data(i, "missed", id)
        missed.append(id)
        id += 1

for missed in missed:
    TextControl.remove_data(missed)

# Zeige Ergebniss
print("\033[92mYour result is here! View output.txt\033[0m")
Result.showresult()
