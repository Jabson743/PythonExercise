price = int(input("Enter the price of the car: "))

if (price < 1000000):
	pay_in_road_tax = price * (10 / 100)
	print(pay_in_road_tax)

if (price >= 1000000 and price <= 3000000):
	pay_in_road_tax = price * (15 / 100)
	print(pay_in_road_tax)

if (price >= 3000000 and price <= 5000000):
	pay_in_road_tax = price * (20 / 100)
	print(pay_in_road_tax)

if (price > 5000000):
	pay_in_road_price = price * (25 / 100)
	print(pay_in_road_tax)        
  
