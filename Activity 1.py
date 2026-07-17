f1=80
f2=90
f3=100
f4=100
f5=110
total=f1+f2+f3+f4+f5
average=total/5
print("Total is:",total,"kg.")
print("Average is:",average,"kg.")

leftover=total%25
bags=total//25
print("Total number of bags:",bags)
print("Leftover grain is:",leftover,"kg.")

lastyr=480
print("More than last year",total>lastyr)
print("Same",total==lastyr)
print("Less than last year",total<lastyr)

total+=30 #Bonus crop
total-=15 #Seed reserve


