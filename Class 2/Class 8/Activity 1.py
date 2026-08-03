print("Welcome to the ride builder!")
choice=input("Please choose whether you want a car or bike:").strip().lower()
if choice=="car":
    car_type=input("What type of car do you want?(Tesla or Audi)").strip().lower()

    if car_type=="tesla":
        print("Great choice!\nThis car is electric and good for the environment.\nSeating Capacity:5 seats")

    elif car_type=="audi":
        print("Nice Choice!!!\nThis car looks cool and is extremely comfortable!\nSeating Capacity:5 seats")

    else:
        print("Please check your input.")

elif choice=="bike":
    bike_type=input("What type of bike would you like?(Motorbike or Scooter)").lower().strip()

    if bike_type=="motorbike":
        print("Great choice!\nMotorbikes are fun and exciting!\nTop Speed:150mph")

    elif bike_type=="scooter":
        print("Nice choice!!!\nThese are safe and comfortable!\nTop Speed:18mph")

    else:
        print("Please check your input.")
else:
        print("Please check your input.")
print("Thank you for using the ride builder! Your vehicle will be with you shortly!")