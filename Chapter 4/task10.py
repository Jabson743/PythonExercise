from random import randint

random_number = randint(1, 1000)
	
guess = 0
stop = " "
counter = 1

print("Welcome To Your Guessing Game")

while (guess != random_number):
	counter + 1
	
	guess = int(input('\n Guess a number between 1 and 1000: '))

	if guess < random_number:
		print('\n Sorry, guess again. Too low.')

	elif guess > random_number:
		print('\n Sorry, guess again. Too high.')

	elif guess == random_number:
		print(f'\n Yay, Congrats. You Have Guessed {random_number} To Be the Right Number Correctly!!! ' )
	print(f"\n You played the Game {counter} times")