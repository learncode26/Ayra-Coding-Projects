print("--- Floyd's Triangle ---")
rows=int(input("Please enter the amount of rows: "))
num=1
for a in range(rows):
    for b in range(a+1):
        print(num,end="\t")
        num+=1
    print()