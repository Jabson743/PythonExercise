number1 = int(input("Enter your first integer: "))
number2 = int(input("Enter your second integer: "))
number3 = int(input("Enter your third integer: "))

sum = number1 + number2 + number3
average = sum / 3
product = number1 * number2 * number3

print("The result of the sum is",sum)
print("The average of the number is", average)
print("The product of the number is", product)

if (number1 < number2 and number1 < number3):
	print(number1,"is the smallest number")

elif (number2 < number1 and number2 < number3):
	print(number2,"is the smallest number")

else:
	print(number3,"is the smallest number")

if (number1 > number2 and number1 > number3):
	print(number1,"is the largest number")

elif (number2 > number1 and number2 > number3):
	print(number2,"is the largest number")

else:
	print(number3,"is the largest number")