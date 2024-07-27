#pseudocode for a program that reads the radius and length of a cylinder

#step 1: initialize the pie value to be 3.14159
#step 2: prompt the user to enter the value of the radius
#step 3: prompt the user to enter the value of the length
#step 4: calculate the result for the value of the area of the cylinder
#step 5: calculate the result for the value of the volume of the cylinder
#step 6: display the result of the radius
#step 7: display the result of the volume

pi = 3.14159

radius = int(input("Enter the value of your radius: "))
length = int(input("Enter the value of your length: "))

area = radius * radius * pi
volume = area * length

print("The area of the cylinder is: ",area)
print("The volume of the cylinder is: ",volume)