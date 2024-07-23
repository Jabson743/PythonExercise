from random import *

number = randint(1, 1000)

sentinel_value = -1

while (number != sentinel_value):

	user_input = int(input("Guess my number between 1 and 1000 with fewest guess: "))

	if (user_input > number):
		print("Too high. Try again")

	if (user_input < number):
		print("Too low. Try again")

	if (user_input == number):
		print("Congratulations. You guess the number!")
		guess_value = input("Press any number to continue or -1 to quit: ")
		

	

		

