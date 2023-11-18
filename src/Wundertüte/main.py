# in main.py
from userinputs import UserInput
from textcontrol import textcontrol

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

if line != inputs[0]:
    for i in range(line+1, inputs[0]+1):
        textcontrol.add_data(i, "missed", id)
        id += 1


print(textcontrol.get_line_data(2))
if 
