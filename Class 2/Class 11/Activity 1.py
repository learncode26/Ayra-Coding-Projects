hundred=fifty=twenty=ten=five=two=one=0
customers_served=0
total_amount=0

serving=True

while serving:
    name=input("Hello, please enter your name:").lower().strip()
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