number = int(input("Enter a five-digit integers: "))

first_integer = (number // 10000)
second_integer = (number // 1000) % 10
third_integer = (number // 100) % 10
fourth_integer = (number // 10) % 10
fifth_integer = (number % 10)

if (first_integer == fifth_integer and second_integer == fourth_integer):

	print(number,"is a palindrome")

else:

	print(number,"is not a palindrome")