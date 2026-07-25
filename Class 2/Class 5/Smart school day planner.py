print("Smart School Day Planner!")

day=input("Please enter the day of the week:").strip().capitalize()
homework=input("Have you finished your homework?(yes/no)").lower().strip()
weather=input("What is the weather like today?(cloudy/sunny/rainy)").lower().strip()
print()
print(f"Your plan for {day}")

if day=="Monday":
    print("It is the start of the week.")

elif day=="Tuesday" or day=="Wednesday" or day=="Thursday":
    print("It is the middle of the week.Stay focused!")

elif day=="Friday":
    print("It is the last school day!")

elif day=="Saturday" or day=="Sunday":
    print("Enjoy your weekend!!!")

else:
    print("Invalid input")

if weather=="sunny" and homework=="yes":
    print("It is nice and sunny today. Head to the park!")

if weather=="rainy" or weather=="cloudy":
    print("Weather tip: Bring an umbella with you if you go out today!")

if not(homework=="yes"):
    print("Please stay in today and finish homework.")

if weather=="rainy" and not(homework=="yes"):
    print("Please stay in today and finish homework.")

elif weather=="sunny" and homework=="yes" and not (day=="Saturday"or day=="Sunday"):
    print("You are all set for your school day! You can go outside and have fun now!")

elif (day=="Saturday"or day=="Sunday") and weather=="sunny":
    print("Perfect weekend weather! Go outside and enjoy!")

else:
    print("Do your homework one step at a time. You can do it!")
print()
print("Your plan is complete! Have a great day!!!")