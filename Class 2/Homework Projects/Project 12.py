total= 4
count = total
print(f"You have {count} homework tasks to finish today!\n")
completed_count = 0
task_num = 1
 
while task_num <= total:
 
    if task_num == 1:
        next_task = "maths worksheet"
    elif task_num == 2:
        next_task = "science reading"
    elif task_num == 3:
        next_task = "English writing"
    else:
        next_task = "coding practice"
 
    answer = input(f"Have you finished your {next_task}? (yes/no): ").strip().lower()
 
    if answer == "yes":
        completed_count += 1
        task_num += 1
        print("Well done! Homework task completed.")
    else:
        print("Hurry up please!")
 
    print("Homework tasks remaining:", total - completed_count)
    print()

print("--- Homework Done! ---")
print("Great work finishing your homework today!\n")

print("Now let's safely peek at an infinite loop...")
test_value = 0
safety_counter = 0
 
while test_value <= 0:
    print("This condition doesn't change, so this would run forever!")
    safety_counter += 1
 
    if safety_counter == 3:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break

print("\n--- Homework Completion Summary! ---")
print("Homework Assigned Today:",count)
print("Homework Completed:", completed_count)
print("Homework Remaining:", total - completed_count)
print()
