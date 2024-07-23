consonant = 0
vowel = 0

words = input("Enter any words to check for the number of consonant and vowel: ")

for character in words:
	if character == "a":
		vowel += 1

	elif character == "e":
		vowel += 1

	elif character == "i":
		vowel += 1

	elif character == "o":
		vowel += 1

	elif character == "u":
		vowel += 1

	else:
		consonant += 1

print("There are", vowel, "vowels and", consonant, "consonant")