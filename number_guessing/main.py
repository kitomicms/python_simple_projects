import random

# guess a number from 1 to 100

# random a number between 1 to 100 first
n = random.randint(1,100)
# store the user input
userinput = int(input("please enter a number from 1 to 100:"))
ubound = 100
lbound = 1

# check if correct answer
while n != userinput:
	if userinput < n:
		lbound = userinput
		print("it is between ",lbound," and ",ubound)
	elif userinput > n:
		ubound = userinput
		print("it is between ",lbound," and ",ubound)
	userinput = int(input("please enter another number:"))	
# congrat user if correct
print("congrats the number is ",n)
# if not tell the user to reenter with hints

# optional: limit the chance user has to guess
