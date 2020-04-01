import random

#Two main variables for project
#By default user_input set to "y" and count set to 0
user_input = "y"
count = 0

#while loop allows for user to continue to play the game and restart
while(user_input == "y"):
    #New random int and intro
    random_number = random.randint(1, 10)
    print(f"Welcome to Guessing Game 1.0\n"
          f"Try to guess the computer's number\n"
          f"Guess a number between 1-10:")
    user_input = int(input())

    #First try if statement
    if(user_input == random_number):
        print("Wow first try!")
        count = None

    #Prompts user for new input with feedback. Also increments count
    while(user_input != random_number):
        if (user_input > random_number):
            count += 1
            print("Lower")
            print("New Guess:")
            user_input = int(input())

        if (user_input < random_number):
            count += 1
            print("Higher")
            print("New Guess:")
            user_input = int(input())

    #Feedback given based on how many guesses it took the user
    if (count == 3) or (count == 4):
        print(f"You got it.\nYou're an ok guesser")
    elif (count < 3):
        print("That was fast")
    elif (count >= 5):
        print("Finally. Your guessing needs work")

    print()
    #play again
    print("Play again? y or n")
    user_input = input()
