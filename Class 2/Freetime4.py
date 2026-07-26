
print()
print("--🏆-High-score Tracker-🏅--")
print()
highscore=0
while True:
    score=int(input("Please enter your score:"))
    print()
    if score>highscore:
        highscore=score
        print("NEW HIGH-SCORE!!!")
        print(f"Your new high-score is {highscore} points!!!")
        print()

    else:
        print("Try again!")
        print()