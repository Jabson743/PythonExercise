def biggest_odd(numbers):

	num_list = [int(num) for num in numbers.split()]

	return max(num_list)

print(biggest_odd("12 4 6 78"))
print(biggest_odd("2 3 5 6 9"))

