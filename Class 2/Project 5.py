temperature = int(input("Enter today's temperature in Celsius: "))

if temperature < 20:
    activity = "indoor reading"
    print("It is cold today.")
    print("Do", activity)
else:
    activity = "outdoor play"
    print("It is hot today.")
    print("Do", activity)
 
raining = input("Is it raining today? (yes/no): ").lower()
 
if raining == "yes":
    print("Choose an indoor activity or carry an umbrella!")
 
homework_time = int(input("Enter homework time in minutes: "))
 
if homework_time > 60:
    needs_break = "yes"
    print("You have a long homework session today.")
    print("Take a short break before your", activity)
else:
    needs_break = "no"
    print("Homework time is short today.")
    print("No long break needed before your", activity)
 
has_free_time = input("Do you have free time today? (yes/no): ").lower()
 
if has_free_time == "yes":
    final_task = "hobby time"
    print("You have free time today.")
    print("Enjoy your", final_task)
else:
    final_task = "planning time"
    print("You do not have much free time today.")
    print("Use some time for", final_task)
 
print("")
 
print("---- DAILY ACTIVITY PLANNER ----")
print("Daily activity check complete!")
print("Temperature:", temperature)
print("Activity Chosen:", activity)
print("Raining:",raining)
print("Study Break Needed:", needs_break)
print("Final Task:", final_task)
