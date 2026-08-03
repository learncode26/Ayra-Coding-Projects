print("Student App Access Manager!")

CAMERA=1
MICROPHONE=2
STORAGE=4
LOCATION=8
approved_apps=["coding app","maths app","music app","study app","reading app","science app","art app"]
restricted_apps=["gaming app","social media app","shopping app"]

name=input("Please enter your name:").strip()
app=input("Please enter the app you want to access:").lower().strip()

print()
print("--- Identity Operator Check ---")

if type(name)is str:
    print("Student's name is stored as text.")

if type(app) is not int:
    print("The requested app is not stored as a number.")

print()
print("--- Membership Operator Check ---")

if app in approved_apps:
    print(app,"is an approved student app.")

else:
    print(app,"is not an approved school app.")



if app in restricted_apps:
    print("Access Denied! App is restricted")

student_permissions=CAMERA|MICROPHONE|STORAGE

print("Permission value:",student_permissions)
print("Permission bits:",bin(student_permissions))

if student_permissions & CAMERA:
    print("Camera permission: Enabled")

if student_permissions & MICROPHONE:
    print("Microphone permission: Enabled")

if student_permissions & STORAGE:
    print("Storage permission: Enabled")

if student_permissions & LOCATION:
    print("Location permission: Enabled")

else:
    print("Location permission: Disabled")


print("\n--- Bit Shift Demonstration ---")
 
next_permission = CAMERA << 1
 
print("Camera bit:", bin(CAMERA))
print("After left shift:", bin(next_permission))
 
previous_permission = STORAGE >> 1
 
print("Storage bit:", bin(STORAGE))
print("After right shift:", bin(previous_permission))
 
 
print("\n--- Final Access Result ---")
 
if app in approved_apps and app not in restricted_apps:
    print("Access granted to", app)
else:
    print("Access denied to", app)
