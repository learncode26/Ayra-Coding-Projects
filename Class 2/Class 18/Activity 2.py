try:
    num1,num2=eval(input("Enter two numbers seperated by a comma: "))
    divide=num1/num2
except ZeroDivisionError as exception:
    print("Avoid entering zero.\n",exception)

except SyntaxError as exception:
    print("This is a syntax error.\n",exception)

except:
    print("Invalid input")

else:
    print("No exception occurred!")

finally:
    print("This will execute no matter what.")