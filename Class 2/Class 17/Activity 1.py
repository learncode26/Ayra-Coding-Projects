print()
print("---Snack Vending Machine!---")
print()
def calc_change(cost,money):
    change=money-cost
    return change
snack_cost=int(input("Enter the cost of your snack: £"))
print("Only £1, £2, £5, £10 coins/notes are accepted.")
num_of_coins=0
money_inserted=0
while True:
    coin=int(input("Enter a coin or note: £"))
    if coin!=10 and coin!=5 and coin!=2 and coin!=1:
        print("Invalid coin inserted. Please enter a valid coin.")
        continue
    money_inserted+=coin
    num_of_coins+=1
    if money_inserted>=snack_cost:
        print("Enough money inserted!")
        break

change_due=calc_change(snack_cost,money_inserted)
print()
print("---Summary of your snack---")
print("The cost of your snack was £",snack_cost)
print("The amount of coins inserted was ",num_of_coins)
print("The amount of money inserted was £",money_inserted)
print("The amount of change was £",change_due)
print()