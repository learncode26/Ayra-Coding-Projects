string=input("Please enter something: ")

reversed=""

for i in string:
    reversed=i+reversed

print(reversed)