item=["pen","sharpener","eraser","glue","paint"]
stock_counts=[1,5,0,31,0]
inventory={item: count for item, count in zip(item,stock_counts)}

print("Full Inventory:", inventory)

in_stock_items = [item for item in item if inventory[item] > 0]
print("Items In Stock:", in_stock_items)

chosen_item=input("Which item do you want to buy?")
if chosen_item not in inventory or inventory[chosen_item] == 0:
    print(chosen_item, "is out of stock! Stopping the checker.")
    exit()

prices=[10,5,40,15,20]

markup=int(input("Enter the markup amount to add to every price: "))

marked_up_prices=list(map(lambda p:p+ markup, prices))
print("Marked up prices :", marked_up_prices)

item_index = item.index(chosen_item)
chosen_price = marked_up_prices[item_index]
print("Price of", chosen_item,"after markup:", chosen_price)

inventory[chosen_item] = inventory[chosen_item]-1
print(chosen_item, "purchased! Remaining stock:", inventory[chosen_item])