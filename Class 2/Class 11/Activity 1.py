hundred=fifty=twenty=ten=five=two=one=0
customers_served=0
total_amount=0

serving=True

while serving:
    print()
    name=input("Hello, please enter your name:").capitalize().strip()
    amount=int(input(f"Hello {name} how much do you want to withdraw: ").strip())
    remaining=amount
    note_index=1
    while note_index<=7:
        if note_index==1:value=100
        elif note_index==2:value=50
        elif note_index==3:value=20
        elif note_index==4:value=10
        elif note_index==5:value=5
        elif note_index==6:value=2
        elif note_index==7:value=1

        count=remaining//value
        if count>0:
            print(f"Dispensing {count} notes of £{value} which is equal to £{count*value}")
            remaining-=count*value
            if note_index==1:hundred+=count
            elif note_index==2:fifty+=count
            elif note_index==3:twenty+=count
            elif note_index==4:ten+=count
            elif note_index==5:five+=count
            elif note_index==6:two+=count
            elif note_index==7:one+=count
        note_index+=1
    customers_served+=1
    total_amount+=amount
    print("Transanction complete",name,"!") 

    ask=input("Is there another customer?(yes/no)").strip().lower()
    if ask!="yes":
        serving=False   

for slot in range(1,8):
    if slot==1:value,total=100,hundred
    elif slot==2:value,total=50,fifty
    elif slot==3:value,total=20,twenty
    elif slot==4:value,total=10,ten
    elif slot==5:value,total=5,five
    elif slot==6:value,total=2,two
    elif slot==7:value,total=1,one
    print(f"Number of {value} notes is {total}.")
    for i in range(total):
        print("=",end="")
    print()
print("Total customers served:",customers_served) 
print("Total amount dispensed:",total_amount)
        