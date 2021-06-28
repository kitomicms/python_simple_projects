# create a input interface to accept email and slice it
input_ = input("pls enter email")
output = input_.split("@")
print("your user name is ", output[0])
print("your client is ",output[1])
