
try:
    num=int(input("Enter a number: "))
    print("Your number is ",num)
except ValueError as exception:
    print("Wrong type of input!\n",exception)