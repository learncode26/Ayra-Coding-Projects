temperature=int(input("Please write the temperature in Celcius:"))

#Decide the outfit based on the weather

if temperature < 20 :
    print("It is cold today")
    outfit="coat"
    print("Wear a",outfit)

else:
    print("It is hot today")
    outfit="t-shirt"
    print("Wear a",outfit)

#Checking the rain

rain=input("Is it raining today? (Yes or no)").lower()
if rain=="yes" :
    print("Bring an umbrella")

#Checking puddles

puddles=input("Are there any puddles? (Yes/No)").lower()

if puddles=="yes" :
    shoes="boots"
    print("Wear boots")

else :
    shoes="trainers"
    print("Wear trainers")

#Summary

print(" ")
print("-----WEATHER OUTFIT PICKER-----")
print("Weather check complete!!")
print("Temperature entered:",temperature)
print("Outfit chosen:",outfit)
print("Raining:",rain)
print("Shoes chosen:",shoes)