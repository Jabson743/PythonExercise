def get_sortedNumbers(num1, num2, num3):

    if num1 > num2:
        num1, num2 = num2, num1
    if num1 > num3:
        num1, num3 = num3, num1
    if num2 > num3:
        num2, num3 = num3, num2

    return num1, num2, num3


print(get_sortedNumbers (30, 20, 10))