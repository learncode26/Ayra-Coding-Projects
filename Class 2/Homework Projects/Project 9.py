print("--🛒-Grocery Cost Comparison Tool!-👜--")
rice=12
milk=4
fruit=8
num_of_baskets=2
family=4

baskets_cost_per_person= ((rice+milk+fruit)*num_of_baskets/family)
print("Grocery basket cost per person:",baskets_cost_per_person)
print()
total_items=int(input("Enter the total number of grocery items:"))
people=int(input("Enter the number of people:"))
 
if total_items % people == 0:
    print(total_items,"items can be divided equally among",people,"people.")
else:
    print(total_items,"items cannot be divided equally among",people,"people.")
 
recorded_average = 65
wrong_week_cost = 50
correct_week_cost = 80
total_weeks = 4
 
recorded_total = recorded_average * total_weeks
 
print("\nRecorded grocery total:", recorded_total)
 
corrected_total = (
    recorded_total
    - wrong_week_cost
    + correct_week_cost
)
 
print("Corrected grocery total:", corrected_total)
 
corrected_average = corrected_total / total_weeks
 
print("Corrected weekly average:", corrected_average)
 
store_a_average = 70
store_b_average = 75
store_c_average = 80
 
print("\nStore A average:", store_a_average)
print("Store B average:", store_b_average)
print("Store C average:", store_c_average)

if (corrected_average < store_a_average and corrected_average < store_b_average and corrected_average < store_c_average):
    print("Your corrected grocery average is lower "
        "than all three store averages.")
 
elif (corrected_average > store_a_average and corrected_average > store_b_average and corrected_average > store_c_average):
    print("Your corrected grocery average is higher "
        "than all three store averages.")
 
else:
    print("Your corrected grocery average is between "
        "the three store averages.")
