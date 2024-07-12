print("Welcome to our online banking")
number = int(input("Enter a number between 1 to 5: "))

match number:
	case 1:
		print("Transfer")

	case 2:
		print("Airtime")
	
	case 3:
		print("Buy Data")

	case 4:
		print("Pay Bills")

	case 5:
		print("Loan")

	case _:
		print("Invalid code")