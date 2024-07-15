passes = 0
failure = 0

while True:
	user_input = int(input("Enter 1 or 2: "))
	if user_input == "1" and user_input == "2":
		passed += 1
		break

	else:
		failure += 1
		print("Please enter a valid input")

		print("Number of passes: ", passes)
		print("Number of failure: ", failure)