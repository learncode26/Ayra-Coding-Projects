total_chores=4
completed_chores=0
chore_num=1
print(f"You have {total_chores} chores to complete today.")

while completed_chores<total_chores:
    if chore_num==1: chore= "making your bed" 
    elif chore_num==2: chore= "doing the dishes" 
    elif chore_num==3: chore= "washing the car" 
    elif chore_num==4: chore= "watering the flowers"
    answer=input(f"Have you finished {chore}?(yes/no)").strip().lower()
    if answer=="yes":
        print("Great job! Keep it up!")
        completed_chores+=1
        chore_num+=1
    else:
        print("Hurry up please!")

    print(f"You have {total_chores-completed_chores} chores left!")

print("All your chores are complete! Well done!")

print("We are looking at an infinite loop!(With safety precautions)")
test_value=0
safety_counter=0
while test_value<=1:
    print("Hi!")
    safety_counter+=1
    if safety_counter==3:
        print("Stopping here on purpose. An actual infinite loop would go on forever!")
        break
print()
print("--------------------")
print("Summary of chores")
print(f"Your total chores are {total_chores}!\nYour remaining chores are {total_chores-completed_chores}!")