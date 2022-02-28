import random

numberToGuess = random.randint(0,50)

print("Welcome to the Random Number Guesser!")

userInput = input("Please guess a number between 0 and 50 ")

alreadyGuessedNumbers = []

# Checks for empty input
if len(userInput) == 0:
  print("Your input cannot be empty")
# Checks for numeric inoput
if userInput.isdigit() == False:
  print("Your inout can only have numbers!")
#checks if you have already guessed a number
if userInput in alreadyGuessedNumbers:
  print("You've already guessed that number!")
# checks if guess is within stated range.
if userInput < 0 or userInput > 50:
  print("Your guess is outside the range")
else:
  print("It's Valid")


# -make sure input is an integer
# -make sure it is numeric, no letters or other chars
# -make sure you dont guess the same number twice.
# no blank guesses
# make sure guess is within the stated range

'''
DATA TYPES
Float - Decimal number
String - Words inside of quotes
Integer - Whole Number, positive, neg, or 0
Boolean - True/False

RULES FOR NAMING VARIABLES
-Only letters, numbers, and underscores
'''

'''
RANDOM NUMBER GUESSER
-The computer will pick a random number between 2 values.
-Then the player will try to guess that number.
-The computer will tell the player if their guess is too high or too low.

What Code Do We Need?
import random
indicate a Range of numbers - min max
Check to see if we have guesed the number or not, if it's too high or too low.
get user input.
make sure that the input is a number
make sure the input is not blank
'''