#  MADE BY:_   
# ░E░l░e░n░a░ ░G░.░ ░Y░a░n░k░o░v░a░
# 'Guess A Number' Game

import random
from colorama import Fore, Back

print("Welcome to Guess A Number game!")
print("I'm thinking of a number between 1 and 100.")
print("You have to guess the number in 7 attempts.")

number = random.randint(1, 100)
guess_count = 0

while guess_count < 7:
    guess = int(input(Fore.LIGHTBLUE_EX + "Enter your guess: "))
    guess_count += 1
    if guess < number:
        print(Fore.LIGHTGREEN_EX + "Your guess is too low.")
    elif guess > number:
        print(Fore.RED + "Your guess is too high.")
    else:
        print(Fore.GREEN + "Congratulations! You guessed the number in", guess_count, "attempts.")
        break

else:  # if guess_count == 8:
    print(Back.LIGHTMAGENTA_EX + "Sorry, you did not guess the number. The number was", number)
