# in userinputs.py
# python module to get the user inputs
userinputs = []

# ask for all amounts (main function in module)


def ask_all():
    ask("Amount of lucky bags")
    ask("Amount of card games")
    ask("Amount of dice games")
    ask("Amount of skill games")

    # ask if continue
    print(
        f"You entered following amounts: Amount of lucky bags:{userinputs[0]} - Amount of card games:{userinputs[1]} - Amount of dice games:{userinputs[2]} - Amount of skill games:{userinputs[3]}")
    Continue = input("Do you want to continue (Y) or correct an input (N)?")
    if Continue == "y" or Continue == "Y":
        return userinputs
    elif Continue == "n" or Continue == "N":
        ask_all()

# get amount of lucky bags


def ask(what):
    userinput = input(f"{what}: ")
    # check if input is valid
    if userinput.isdigit():
        # if yes add input to answer list
        userinputs.append(int(userinput))
    else:
        # if no restart the user input function
        print("You didn't enter a valid number. Please enter a number.")
        ask(what)


# run user input functions if code is not runned as module
if __name__ == "__main__":
    print(ask_all())
