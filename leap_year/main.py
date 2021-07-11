while True:
  user_input = int(input("Enter a year"))
  if (user_input % 4 == 0) and (user_input%100 == 0) and (user_input%400 ==0):
    print(user_input,"it is a leap year", user_input%4, user_input%100, user_input%400)
    print(user_input//4)
    print(user_input//100)
    print(user_input//400)
  else:
    print("it is not a leap year")
