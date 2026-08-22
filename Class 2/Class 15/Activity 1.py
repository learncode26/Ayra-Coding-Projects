def greet_customer():
    print("Welcome to the lemonade stand!\nFresh lemonade here!")

greet_customer()

price=float(input("What is the price per cup? £"))
cups=int(input("How many cups did you buy? ")) 

def total_amount(cost,quantity):
    total=cost*quantity
    return total

total=total_amount(price,cups)

rounded_total=round(total,2)
print("Your total is £",rounded_total)
payment=float(input("How much have you paid? £"))

def change_due(paid,totalcost):
    change=paid-totalcost
    return change

change=change_due(payment,rounded_total)

def closing (cups):
    if cups>=5:
        print("Thank you for all your support! Bye!")
    else:
        print("Thank you for visiting our stall. Bye!")

print()
print("==============================")
print("  LEMONADE STALL RECEIPT!!!")
print("==============================")
print("Price per cups : £",price)
print("Number of cups : ",cups)
print("Your total cost: £",rounded_total)
print("Amount paid    : £",payment)
print("Change due     : £",change)
print()
closing(cups)