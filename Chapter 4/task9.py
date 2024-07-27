def fahrenheit_temperature(celsius):

    fahrenheit = (celsius * 9 / 5) + 32

    return fahrenheit

print(" Celsius  |  Fahrenheit ")

print("-" * 25)

for celsius in range(1, 101):

    fahrenheit = fahrenheit_temperature(celsius)

    print(f"{celsius: 8}  |  {fahrenheit: 5}")