basket1={"strawberry","blueberry","kiwi","orange"}
basket2={"apple","banana","strawberry","apple"}

print(basket1)
print(basket2)

basket2.add("orange")

print(basket2)

b3=basket1.intersection(basket2)

print(b3)

import array as arr

fruits=arr.array("h",[2,5,7,6,9,7,1,4,8])

print(fruits)

fruits.insert(0,1)

fruits.append(6)

print(fruits)

count_7=fruits.count(7)
print(count_7)

fruits.reverse()
print(fruits)