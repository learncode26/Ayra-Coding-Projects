t1=10
t2=20
t3=30
t4=10
t5=30

total=t1+t2+t3+t4+t5
average=total/5

print("The sum of all the points is",total)
print("The average is",average)

stars_per_point=5
stars=total*stars_per_point
print("Total stars:",stars)
boxes=stars//25
leftover=stars%25
print("Full boxes packed:",boxes)
print("Leftover stars:",leftover)

last_week_points=150

print("Better than last week?",total > last_week_points)
print("Same as last week?",total == last_week_points)
print("As least as good?",total <= last_week_points)

total+=30
print("After bonus:",total)

total-=15
print("After points taken:",total)

stars=total*stars_per_point
boxes=stars//25
print("Boxes packed:",boxes)