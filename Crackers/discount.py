def my_discount(price, discount):

	discount_price = price * (discount / 100)

	price_after_discount = price - discount_price

	return price_after_discount

print(my_discount(150, 15))