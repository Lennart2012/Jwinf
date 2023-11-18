# in userinputs.py
# python module to get the user inputs
userinputs = []

# ask for all amounts (main function in module)


class UserInput():
    def ask_all():
        UserInput.ask("Amount of lucky bags")
        UserInput.ask("Amount of dice games")
        UserInput.ask("Amount of card games")
        UserInput.ask("Amount of skill games")
        return userinputs

    def ask(what):
        userinput = input(f"{what}: ")
        # check if input is valid
        if userinput.isdigit():
            # if yes add input to answer list
            userinputs.append(int(userinput))
        else:
            # if no restart the user input function
            print("You didn't enter a valid number. Please enter a number.")
            UserInput.ask(what)

# get amount of lucky bags


# run user input functions if code is not runned as module
if __name__ == "__main__":
    print(UserInput.ask_all())
