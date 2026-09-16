print("Calculator")
asmd=input("Do you want to add subtract multipy or divide? (+,-,*,/)")
try:
    num1=float(input("Enter a number:"))
    num2=float(input("Enter a number:"))
except ValueError:
    print("Please enter a NUMBER")
def add(n1,n2):
    answer=n1+n2
    return answer
def subtract(n1,n2):
    answer=n1-n2
    return answer
def multiply(n1,n2):
    answer=n1*n2
    return answer
def divide(n1,n2):
    try:
        answer=n1/n2
        return answer
    except ZeroDivisionError:
        print("You cannot divide by ZERO")

if asmd=="+":
    print(add(num1,num2))
elif asmd=="-":
    print(subtract(num1,num2))
elif asmd=="*":
    print(multiply(num1,num2))
elif asmd=="/":
    print(divide(num1,num2))
else: print("Invalid input!")
