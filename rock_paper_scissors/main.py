# make a input
import random
choice = ['rock','paper','scissors']
while True:
  user_input = input("Choose one: rock/paper/scissors")
  computer_input = choice[random.randint(0,2)] 
  if user_input == computer_input:
    print("Draw")
  elif user_input == "rock":
    if computer_input == "scissors":
      print("Computer choose", computer_input, "You win !")
    else:
      
      print("Computer choose", computer_input, "You lose !")
  elif user_input == "scissors":
    if computer_input == "rock":
      print("Computer choose", computer_input, "You lose !")
    else:
      print("Computer choose", computer_input, "You win !")
      
  elif user_input == "paper":
    if computer_input == "rock":
      print("Computer choose", computer_input, "You win !")

    else:
      print("Computer choose", computer_input, "You lose !")
  else:
    print("Please enter again")
    




