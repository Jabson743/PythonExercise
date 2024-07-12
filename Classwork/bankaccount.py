print("Welcome to your online banking")

deposit = 0
withdraw = 0
balance = 0

while(True):

	account = int(input('''1. Deposit
2. Withdraw
3. Balance
'''))

	match (account):
		case 1:
			print("Deposit")
			deposit = int(input("Enter the amount you want to deposit: "))
			balance += deposit
			print("Your available balance is", balance)

		case 2:
			print("Withdraw")
			withdraw = int(input("Enter the amount you wished to withdraw: "))
			if withdraw == 0:
				print("Insuuficient balance")
			if withdraw < 0:
				print("Insufficient balance")
			if withdraw > balance:
				print("Insufficient balance")
			balance -= withdraw
			
		case 3:
			print("Balance")
			if balance == 0:
				print("You have a low balance")
			if balance < 0:
				print("Insufficient balance")
			print("Your available balance is", balance)
			break

		case 99:
			print("Invalid code, kindly enter a valid code")
			print("Do you wish to perform another transaction")