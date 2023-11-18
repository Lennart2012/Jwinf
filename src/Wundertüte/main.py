# in main.py
from userinputs import *
from textcontrol import *

inputs = UserInput.ask_all()
print(inputs)

textcontrol.create_framework(inputs[0])
line = 0
id = 0

for dice_game in range(1, inputs[1]+1):
    if line == inputs[0]:
        line = 1
    else:
        line += 1

    textcontrol.add_data(line, "Dice Game", id)
    id += 1
