l1=[1,7,3,0,2,5,6,9]

sum=0

for i in l1:
    sum+=i

d=len(l1)
average=sum/d
print(f"The sum of the list is {sum}.\nThe average of the list is {average}.")

l1.sort()
s=l1[0]
b=l1[-1]
print(f"The smallest value in the list is {s}.\nThe largest value in the list is {b}.")
