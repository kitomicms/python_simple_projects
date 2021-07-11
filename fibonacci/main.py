while True:
  userInput = int(input("please enter a number: "))
  n = [1,1]
  while n[-1] < userInput:
    n.append(n[-1]+n[-2])
    if n[-1] == userInput:
      print("it is in the fibonacci sequense")
      break
  if n[-1] > userInput:
     print("it is not in the fibonacci sequense")
