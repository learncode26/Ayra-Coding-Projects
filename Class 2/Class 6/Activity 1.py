x=20
if type(x) is int:
    print("True")

else:
    print("False")

a=3.5
if type(a) is not float:
    print("True")

else:
    print("False")

o=60
n=60
if o is n:
    print("O and N have the SAME identity!")

n=10
if o is not n:
    print("O and N have DIFFERENT identities.")