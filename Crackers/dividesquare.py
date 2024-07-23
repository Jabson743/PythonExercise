def divide_or_square(number):

	square_root = ''
	remainder = ''

	if (number % 5 == 0):
		square_root = number ** 2
		return square_root

	else:
		remainder = number % 5
		return remainder

print(divide_or_square(10))