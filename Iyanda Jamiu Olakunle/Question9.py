name = input("Enter employee's name: ")
hours_worked = float(input("Enter number of hours worked in a week: "))
hourly_pay = float(input("Enter the hourly pay rate: "))
federal_tax = float(input("Enter the federal tax withholding rate: "))
state_tax = float(input("Enter the state tax withholding rate: "))

hourly_pay = 10 * hours_worked 
federal_tax = 20 / 100 * 97.5
state_tax = 9 / 100 * 97.5
total_deduction = federal_tax + state_tax

net_pay =  hourly_pay - total_deduction

print(net_pay)