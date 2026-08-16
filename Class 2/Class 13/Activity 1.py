print("---The Diamond Pattern---")

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
