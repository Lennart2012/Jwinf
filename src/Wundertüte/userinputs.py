#python module to get the user inputs
userinputs = []
#ask for all amounts (main function in module)
def ask_all():
    ask("Lucky bags")
    ask("Card games")
    ask("Dice games")
    ask("Skill games")
    
    #ask if continue
    print("You entered following amounts:" + " Amount of lucky bags:" + userinputs[0] + " Amount of card games:" + userinputs[1] + " Amount of dice games:" + userinputs[2] + " Amount of skill games:" + userinputs[3])  
    Continue = input("Do you want to continue (Y) or correct a input (N)?")
    if Continue == "y" or Continue == "Y":
        return userinputs
    elif Continue == "n" or Continue == "N":
        ask()
        
    
#get amount of lucky bags
def ask(what):
    userinput = input("amount of " + what)
    #check if input is vaild
    if userinput.isdigit():
        #if yes add input to answer list
        userinputs.append(userinput)
    else:
        #if no restart the user input function
        print("You didn't entered a vaild number. Please enter a number.")
        ask(what)

#run user input functions if code is not runned as module
if __name__ == "__main__":
    print(ask())