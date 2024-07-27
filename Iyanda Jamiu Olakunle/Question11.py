number = int(input("Enter a valid integer: "))

if (number % 5 == 0 and number % 6 == 0):
	print("True")

if(number % 5 == 0 or number % 6 == 0):
	print("False")

print(number)
