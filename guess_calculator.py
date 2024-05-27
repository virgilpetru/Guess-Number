from art_guess_calculator import logo
import random
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
win_number = random.randint(1, 100)
should_stop = False
if difficulty == "easy":
    print(f"You have 10 attempts to guess the number.")

    while should_stop == False:
        attempts = 10
        count = 0
        while attempts > 0:
            number = input("Make a guess: ")
            if number > str(win_number):
                attempts -= 1
                count += 1
                print("Too high.\n Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
            elif number < str(win_number):
                count += 1
                attempts -= 1
                print("Too low.\n Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
            elif number == str(win_number):
                print("You win!")
                exit()
        if attempts == 0:
            print("You lost!")
            exit()

elif difficulty == "hard":
    print("You have 5 attempts to guess the number")

    while not should_stop:
        attempts = 5
        count = 0
        while attempts > 0:
            number = input("Make a guess: ")
            if number > str(win_number):
                attempts -= 1
                count += 1
                print("Too high.\n Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
            elif number < str(win_number):
                count += 1
                attempts -= 1
                print("Too low.\n Guess again.")
                print(f"You have {attempts} attempts remaining to guess the number.")
            elif number == (str(win_number)):
                print("You win!")
                exit()
        if attempts == 0:
            print("You lost!")
            exit()