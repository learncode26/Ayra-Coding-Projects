print("-----Library Planner!!!-----")

day=input("What day is it today?").strip().capitalize()
weather=input("What is the weather like today?(sunny/cloudy/rainy)").lower().strip()
book=input("Do you need to return a book?(yes/no)").strip().lower()
print()
print("Output:")

if day in ("Saturday", "Sunday"):
    print("It's the weekend! You can have a relaxed library visit.")

elif day=="Monday":
    print("It is the start of the week! Please check your reading list.")

elif day in ("Tuesday","Wednesday","Thursday"):
    print("It is a normal school day! Plan a short library visit if you can.")

elif day=="Friday":
    print("It's the last school day! You should return your books before the weekend.")

else:
    print("Please check your spelling!")

if weather=="sunny" and book=="yes":
    print("Tip: Nice weather! You should visit the library today as you have a book due!")

if weather=="cloudy" or weather=="rainy":
    print("If you visit the library then bring an umbrella with you please.")

if not (book=="yes"):
    print("You don't need to return any books. You can browse new books today!")
print()

print("Best plan:")
if weather=="rainy" and book=="yes":
    print("Go to the library to return on your book on time and use a car or bus to travel there.")

elif weather=="sunny" and book=="yes" and not(day in("Saturday","Sunday")):
    print("Go to the library after school and return your book.")

elif day in("Saturday","Sunday") and weather=="sunny":
    print("Perfect weather for a long,calm library visit!")

else:
    print("Check your schedule and plan a library visit.")

print()

print("Library plan complete! Happy reading!")

print()