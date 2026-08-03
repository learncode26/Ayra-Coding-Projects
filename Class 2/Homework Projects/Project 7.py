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
