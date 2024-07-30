number = int(input("Enter a number: "))

def palindrone(number):

	if(number / 100 == 1 and number % 10 == 1):
		return("It is a palindrone")

	else:
		return("It is not a palindrone")

print(palindrone(number))

	