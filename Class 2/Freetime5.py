print()
print("---Prime Number Checker!---")
print()

n = int(input("Please enter a number: "))

if n == 2 or n == 3 or n == 5 or n == 7:
    print("This is a prime number!!!")

else:
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        print("This is not a prime number!")

    else:
        print("This is a prime number!!!")

print()
print("Prime number check complete!")