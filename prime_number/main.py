# enter a number and return True/False
# prime number
while True:
  userInput = int(input("Please enter a number: "))
  counter = 0
  for i in range(1,userInput+1):
    if userInput % i == 0:
      counter += 1
      
  if counter == 2:
    print("it is a prime number") 
  else:
    print("it is not a prime number")

