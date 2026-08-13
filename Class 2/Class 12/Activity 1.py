print("---Right Angled Triangle---")
rows=int(input("Please enter the amount of rows: "))

for a in range(rows):
    for b in range(a+1):
        print("*",end="")
    print()