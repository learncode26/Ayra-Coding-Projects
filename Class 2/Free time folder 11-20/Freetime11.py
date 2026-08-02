print()
print("NHS Blue Light Discount Calculator!")
print("")
cost=float(input("Please enter the price of your meal(in pounds):"))
percentage=float(input("Please enter the percentage of the discount:"))

if percentage>14:
    print("That is not possible, please try again.")
    exit()

total=percentage/100 * cost
final=cost-total
print(f"You have to pay £{final} pounds with the discount!")
print()
print("Bye!")
print()
