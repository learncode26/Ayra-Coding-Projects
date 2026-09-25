print()
print("-🕹️  🎮-Text Adventure Game-👾  🎲-")
name=input("Please enter your name, explorer : ").capitalize().strip()
print(f"Hello {name} in this game you are stranded in a forest with no way of escaping unless you risk your life to make choices, solve clues and solve the puzzle.\nGood luck,explorer {name}!")
choice1=int(input("You are trekking through the Amazon Rainforest for days in search of a secret temple built billions of years ago. You are heading in the right direction according to your map.\nHowever, as you admire the view, a stealthy monkey grabs your map!!!\nWhat do you do(1/2)?\n1)Chase after the monkey!\n2)Climb up a tree!"))
if choice1==1:
    choice2=int(input("You chase after it: you know you are lost without the map! However, your eye caught sight of a banana tree!\nWhat do you do?(1/2)\n1)You keep going after the monkey, it might run out of your sight if you get distracted!\n2)You grab a banana and lure it back!"))
    if choice2==1:
        print("As you chase behind it, the monkey clambers up a tree and disappears behind the foliage! You look around,wondering what to do next when you find a tiger prowling right behind you!\n 💀 GAME OVER! 💀 ")
    elif choice2==2:
        print("You grab a banana and the monkey races towards you however following it is the rest of the monkey troop!\nWhat do you do?\n1)Throw the banana away!\n2)Stand still!?")





