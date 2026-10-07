weather=(1,0,0,1)
rainy=0
sunny=0
# rainy is 1 and sunny is 0
for i in weather:
    if i == 1:
        rainy+=1
    else:
        sunny+=1

if rainy>sunny:
    print("It is rainy! Bring an umbrella!")
elif rainy==sunny:
    print("It is both rainy and sunny! You can see a rainbow!")
else:
    print("It is sunny! Wear a hat!")