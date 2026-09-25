
print()
def matchword(list1):
    answer=[]
    for word in list1:
        if len(word)>1 and word[0]==word[-1]:
            answer+=[word]
    print(f"This is the list of words that have the first character the same as the last character and are more than 1 character long:\n{answer}")
    return len(answer)
l=["cat", "anaconda","teapot","keyboard","noun","dogs","rear" ]
len_answer= matchword(l)
print(len_answer)
print()