print("Factorials!")

def factorials(num):
    if num==1 or num==0:
        return 1
    else:
        return num*factorials(num-1)
number=int(input("Enter a number: "))
print(factorials(number))