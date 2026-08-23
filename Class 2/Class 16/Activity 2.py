print("Cube Calculator")

def cube(num):
    return num*num*num

def by_three(num):
    if num%3==0:
        return cube(num)
    else:
        return False

number=int(input("Enter a number: "))
print(by_three(number))