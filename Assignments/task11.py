number = int(input("Enter your integer: "))

digit5 = (number // 1 % 10)
digit4 = (number // 10 % 10)
digit3 = (number // 100 % 10)
digit2 = (number // 1000 % 10)
digit1 = (number // 10000 % 10)

print(digit1, " " , digit2, " " , digit3, " " , digit4, " " , digit5)
