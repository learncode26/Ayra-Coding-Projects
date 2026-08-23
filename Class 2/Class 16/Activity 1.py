print("---Tip The Waiter---")

def total_money(tip_perc,bill_cost):
    total=tip_perc/100*bill_cost+bill_cost
    return total

bill=float(input("Enter the bill: £"))
tip=int(input("Enter the tip percentage: "))

print("£",total_money(tip,bill))