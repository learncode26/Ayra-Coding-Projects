print()
print("Welcome to the bill calculator!")
print()
cost=int(input("Please enter the cost in pounds:"))
number=int(input("Please enter the number of people:"))
Tip=(input("Do you want to add a tip(yes/no)?"))
if Tip=="yes":
    tip=int(input("How much do you want to add as a tip(in pounds)?"))

else:
    tip=0

total_cost=tip+cost
each_cost=round(total_cost/number,2)
print()
print(f"The cost per person is £{each_cost}!")
print()
print("Thank you for using the bill calculator!")
print()