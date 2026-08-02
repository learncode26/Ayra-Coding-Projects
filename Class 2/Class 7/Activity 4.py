#Getting the input from the user
a=int(input("Please enter the speed: "))
b=int(input("Please enter the speed: "))
c=int(input("Please enter the speed: "))

#Getting the average
average=(a+b+c)/3
print("The average is",average)

#Comparing the average with the different speeds

if average>a and average>b and average>c:
    print("%d is higher than %d,%d,%d." %(average,a,b,c))

elif average>a and average>b :
    print("%d is higher than %d,%d." %(average,a,b))

elif average>a and average>c :
    print("%d is higher than %d,%d." %(average,a,c))

elif average>c and average>b :
    print("%d is higher than %d,%d." %(average,b,c))

elif average>a :
    print("%d is higher than %d." %(average,a))

elif average>b :
    print("%d is higher than %d." %(average,b))

elif average>c :
    print("%d is higher than %d." %(average,c))

else:
    print("Invalid input!")