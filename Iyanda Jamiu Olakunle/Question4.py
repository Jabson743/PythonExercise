#A program that reads the subtotal and the gratuity rate

#step 1: initialize the gratuity rate value
#step 2: initialize the total value
#step 3: prompt the user to enter a value
#step 4: multiply the number by the value of the gratuity rate 
#step 5: add the result of the gratuity by the user input to get the value of the total
#step 6: display the result of the gratuity
#step 7: display the result of the total

number = int(input("Enter a valid number: "))

gratuity_rate = 15 / 100
total = 0

gratuity = number * gratuity_rate
total = gratuity + number

print("The value of the gratuity is: ",gratuity)
print("The value of the total is: ",total)

