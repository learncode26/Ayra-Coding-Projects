print("-⭐- Star Pattern -⭐-")
rows=int(input("Enter the number of rows:"))
for i in range(rows):
    for j in range(i+1):
        print("*",end="")
    print()
print()
print("-♦️- Diamond Pattern -♦️-")
rows=int(input("Enter the amount of rows please: "))
if rows%2==0:
    half=rows//2
else:
    half=(rows+1)//2
space=half-1
for i in range(1,half+1):
    for j in range(space):
        print(" ",end="")
    space-=1
    num=1
    for k in range(2*i-1):
        print(num,end="")
        num+=1
    print()
space=1
for i in range(1,half):
    for j in range (1,space+1):
        print(" ",end="")
    space+=1
    num=1
    for k in range(1,(half-i)*2):
        print(num,end="")
        num+=1
    print()
print()
print("-🔼- Floyd Triangle -🔼-")
rows=int(input("Please enter the amount of rows: "))
num=1
for a in range(rows):
    for b in range(a+1):
        print(num,end="\t")
        num+=1
    print()
print()
