print()
print("Number Calculator!")
print()
num1=int(input("Please enter your first number:"))
num2=int(input("Please enter your second number:"))
num3=int(input("Please enter your third number:"))
num4=int(input("Please enter your last number:"))

total=num1+num2+num3+num4
average=round(total/4,2)

largest=num1

if num2>largest:
    largest=num2

if num3>largest:
    largest=num3

if num4>largest:
    largest=num4
print()
print("The largest number is",largest)

smallest=num1

if num2<smallest:
    num2=smallest

if num3<smallest:
    num3=smallest

if num4<smallest:
    num4=smallest

num_range=largest-smallest
print("The smallest number is",smallest)

print("The sum of all the numbers are",total)

print("The average of all the numbers is",average)

print("The range of all the numbers is",num_range)

print()
print("Thank you for using the number calculator! Bye!!!")
print()