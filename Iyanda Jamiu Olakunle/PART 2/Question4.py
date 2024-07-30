number = int(input("Enter a number: "))

def even_odd(number):

	if(number % 2 == 0):
		return("it is an even number")

	else:
		return("it is an odd number")

print(even_odd(number))