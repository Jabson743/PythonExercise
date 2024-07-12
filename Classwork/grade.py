grade = int(input("Please enter your grade score: "))

if (grade >= 75):
	print("A")

elif (grade >= 65 and grade < 75):
	print("B")

elif (grade >= 50 and grade < 65):
	print("C")

elif (grade >= 40 and grade < 50):
	print("D")

else: 
	print("Fail")


#counter = 0
#while (counter <= 10):
      #print(counter)
      #counter += 1

total = 0
counter = 0
score = int(input("Enter your score: "))

while (score != -1):
      counter += 1
      total += score
      score = int(input("Enter your score: "))
      
      average = total / counter

      print(average)