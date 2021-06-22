# roll a dice

import random

n = random.randint(1,6)
m = "Y"
print(n, " is rolled")
m = input("another roll? Y/N: ")

while m == "Y":
	n = random.randint(1,6)
	print(n, " is rolled")
	m = input("another roll? Y/N: ")
