number = int(input("Enter a number: "))

for digit in range(1, 11):
	result = number * digit
	print(f"{number} * {digit} = {result}")