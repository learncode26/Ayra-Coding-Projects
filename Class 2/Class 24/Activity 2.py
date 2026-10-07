def palindrome(tup):
    start=0
    end=len(tup)-1
    while start<end:
        if tup[start]!=tup[end]:
            return False
        start+=1
        end-=1
    return True
tuples=(5,6,7,6,5)
if palindrome(tuples):
    print("This tuple is a palindrome!")
else :
    print("This tuple is not a palindrome.")