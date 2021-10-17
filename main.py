from random import randint


userWins = 0
ComputerWins = 0
Ties = 0


def RPC(input):
    global userWins, ComputerWins, Ties
    compChoice = randint(1, 3)
    userChoice = input

    if userChoice == "R" and compChoice == 3:
        #print("User wins, rock beats scissor")
        userWins += 1

    elif userChoice == "R" and compChoice == 2:
        #print("Computer wins, paper beats rock")
        ComputerWins += 1

    elif userChoice == "R" and compChoice == 1:
        #print("It's a tie, both chose Rock")
        Ties += 1

    elif userChoice == "P" and compChoice == 3:
        #print("Computer wins, scissor beats paper")
        ComputerWins += 1

    elif userChoice == "P" and compChoice == 2:
        #print("It's a tie, both chose paper")
        Ties += 1

    elif userChoice == "P" and compChoice == 1:
        #print("User wins, paper beats rock")
        userWins += 1

    if userChoice == "S" and compChoice == 3:
        #print("It's a tie, both chose scissors")
        Ties += 1

    elif userChoice == "S" and compChoice == 2:
        #print("User wins, scissor beats paper")
        userWins += 1

    elif userChoice == "S" and compChoice == 1:
        #print("Computer wins, rock beats scissors")
        ComputerWins += 1


userChoice = input("Enter R for Rock, P for paper, S for Scissor: ").upper()

#ranger = 10000000

#for _ in range(ranger):
#    RPC(userChoice)

RPC(userChoice)
print("\nUser Wins: " + str(userWins))
print("Computer Wins: " + str(ComputerWins))
print("Ties: " + str(Ties))
