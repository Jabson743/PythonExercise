passes = 0
fail = 0

while True:
	for number in range(1, 16):
		scores = int(input("Enter your score: "));
		if scores >= 45:
			passes += 1
			break
		else:
			fail +=1

			print("Number of passes: ", passes)
			print("Number of failure: ",fail)