principal = int(input("Enter the principal amount: "))
double_rate = float(input("Enter the annual interest rate: "))
duration = int(input("Enter the duration in years: "))

monthly_payment = principal * double_rate(1 + double_rate) ** duration 

print(monthly_payment)
