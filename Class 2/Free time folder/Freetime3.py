print()
print("--🧮-💯-Percentage Calculator!-➕-📖--")
print()
maths=int(input("Please enter your score for MATHS (out of 100)"))
if maths>100 or maths<0:
    print("Invalid input!")
    exit()
english=int(input("Please enter your score for ENGLISH (out of 100)"))
if english>100 or english<0:
    print("Invalid input!")
    exit()
science=int(input("Please enter your score for SCIENCE (out of 100)"))
if science>100 or science<0:
    print("Invalid input!")
    exit()
art=int(input("Please enter your score for ART (out of 50)"))
if art>50 or art <0:
    print("Invalid input!")
    exit()
music=int(input("Please enter your score for MUSIC (out of 50)"))
if music>50 or  music<0:
    print("Invalid input!")
    exit()
spanish=int(input("Please enter your score for SPANISH (out of 75)"))
if spanish>75 or spanish <0:
    print("Invalid input!")
    exit()
pe=int(input("Please enter your score for PE (out of 75)"))
if pe>75 or pe <0:
    print("Invalid input!")
    exit()
print()
maths_score=maths
english_score=english
science_score=science
art_score=art*2
music_score=music*2
spanish_score=round(spanish/3*4,2)
pe_score=round(pe/3*4,2)
print(f"Your score for MATHS was {maths_score}%")
print(f"Your score for ENGLISH was {english_score}%")
print(f"Your score for SCIENCE was {science_score}%")
print(f"Your score for ART was {art_score}%")
print(f"Your score for MUSIC was {music_score}%")
print(f"Your score for SPANISH was {spanish_score}%")
print(f"Your score for PE was {pe_score}%")
total=maths+english+science+art+music+spanish+pe
average=round(total/550*100,2)
print(f"Your average percentage is {average}%")
print()
if average<25:
    print("Lots of room for improvement. Try harder next time.")

elif average<60:
    print("You did okay but try harder next time.")

elif average<70:
    print("Nice try!")

elif average<80:
    print("Well done! You did a good job!")

elif average<90:
    print("Brillant Job!!!")

else:
    print("AMAZING SCORE!!! WOW!!!")

print()






