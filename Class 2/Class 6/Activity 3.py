mark1=int(input("What is your marks for subject 1?"))
mark2=int(input("What is your marks for subject 2?"))
mark3=int(input("What is your marks for subject 3?"))
mark4=int(input("What is your marks for subject 4?"))
mark5=int(input("What is your marks for subject 5?"))
total=mark1+mark2+mark3+mark4+mark5
average=total//5
valid_range=range(101)
if average not in valid_range:
    print("Invalid input!")

elif average in range(75,101):
    print("Well done! Excellent performance!")

elif average in range(50,75):
    print("Average performance.")

else:
    print("Poor performance.")