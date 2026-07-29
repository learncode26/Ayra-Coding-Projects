# print()
# print("Welcome to the text adventure game!")
# print()
# setting=input("Please enter the setting of your adventure(mountains/desert/forest):").strip().lower()
# pet=input("Please enter your type of pet(dog/cat):").strip().lower()
# print()
# print("---Welcome to your adventure---")
# print(f"You are lost in the {setting} with no food, no water or any way to get back home! All you have is your faithful pet {pet}, a compass, a torch, a knife, a rope and a zipline hook. Make the right choices or else you will face certain doom... ")
# # print("")
print()
print("🌍 WELCOME TO THE TEXT ADVENTURE GAME! 🌍")
print()

setting = input("Please enter the setting of your adventure (mountains/desert/forest): ").strip().lower()
pet = input("Please enter your type of pet (dog/cat): ").strip().lower()

print()
print("--- Welcome to your adventure! ---")
print()

print(f"You are lost in the {setting} with no food, no water,")
print(f"or any way to get back home!")
print(f"All you have is your faithful pet {pet},")
print("a compass, a torch, a knife, a rope and a zipline hook.")
print()
print("Make the right choices or else you will face certain doom...")
print()


# MOUNTAINS ADVENTURE
if setting == "mountains":

    print("🏔️ You begin climbing the mountain.")
    print("The weather is getting colder and snow begins to fall.")
    print()

    choice = input("You see a cave and a mountain path. Do you choose the cave or the path? ").strip().lower()

    if choice == "cave":

        print()
        print("You and your pet enter the dark cave.")
        print("You turn on your torch and discover a mysterious tunnel.")
        print()

        choice = input("Do you explore the tunnel or leave the cave? ").strip().lower()

        if choice == "explore":
            print()
            print("You explore the tunnel and discover a hidden treasure chest!")
            print("Inside the chest is food, water and a map showing the way home!")
            print()
            print("🎉 YOU WIN! 🎉")

        if choice == "leave":
            print()
            print("You leave the cave, but a snowstorm suddenly begins.")
            print("You and your pet become lost in the mountains.")
            print()
            print("💀 GAME OVER! 💀")

    if choice == "path":

        print()
        print("You follow the mountain path.")
        print("Suddenly, the path ends at a huge gap in the mountain!")
        print()

        choice = input("Do you use your rope or your zipline hook? ").strip().lower()

        if choice == "rope":
            print()
            print("You use your rope to climb carefully across the gap.")
            print("You make it safely to the other side!")
            print("You find a rescue station and finally get home.")
            print()
            print("🎉 YOU WIN! 🎉")

        if choice == "zipline":
            print()
            print("You attach your zipline hook and launch yourself across.")
            print("Unfortunately, the rope breaks halfway across!")
            print()
            print("💀 GAME OVER! 💀")


# DESERT ADVENTURE
if setting == "desert":

    print("🏜️ You begin walking through the scorching desert.")
    print("The sun is extremely hot and you are becoming very thirsty.")
    print()

    choice = input("You see an old building and a tall cactus. Do you choose the building or cactus? ").strip().lower()

    if choice == "building":

        print()
        print("You enter the old building.")
        print("Inside, you discover an old water bottle!")
        print("Your pet is very happy to have some water.")
        print()

        choice = input("Do you stay in the building or continue exploring? ").strip().lower()

        if choice == "stay":
            print()
            print("You decide to stay until the sun goes down.")
            print("When it becomes cooler, you use your compass to find your way home.")
            print()
            print("🎉 YOU WIN! 🎉")

        if choice == "explore":
            print()
            print("You leave the building and continue walking.")
            print("Unfortunately, you become lost in the huge desert.")
            print()
            print("💀 GAME OVER! 💀")

    if choice == "cactus":

        print()
        print("You walk towards the cactus.")
        print("Behind it, you discover a hidden oasis!")
        print("There is fresh water and a small boat.")
        print()

        choice = input("Do you drink the water or take the boat? ").strip().lower()

        if choice == "drink":
            print()
            print("You and your pet drink the fresh water.")
            print("You feel strong enough to continue your journey.")
            print("You follow your compass and find your way home.")
            print()
            print("🎉 YOU WIN! 🎉")

        if choice == "boat":
            print()
            print("You take the boat onto the oasis.")
            print("Unfortunately, the boat has a huge hole in it!")
            print()
            print("💀 GAME OVER! 💀")


# FOREST ADVENTURE
if setting == "forest":

    print("🌲 You enter a dark and mysterious forest.")
    print("You hear strange noises coming from behind you.")
    print()

    choice = input("You see a river and a wooden bridge. Do you choose the river or bridge? ").strip().lower()

    if choice == "river":

        print()
        print("You walk towards the river.")
        print("The water is moving very quickly.")
        print()

        choice = input("Do you cross the river or follow it? ").strip().lower()

        if choice == "cross":
            print()
            print("You carefully cross the river with your pet.")
            print("On the other side, you find a cabin!")
            print("Inside the cabin is a radio.")
            print("You use the radio to call for help.")
            print()
            print("🎉 YOU WIN! 🎉")

        if choice == "follow":
            print()
            print("You follow the river deeper into the forest.")
            print("You become completely lost.")
            print()
            print("💀 GAME OVER! 💀")

    if choice == "bridge":

        print()
        print("You walk carefully across the old wooden bridge.")
        print("Suddenly, you hear a loud CRACK!")
        print()

        choice = input("Do you run forward or turn back? ").strip().lower()

        if choice == "run":
            print()
            print("You run as fast as you can!")
            print("You and your pet make it safely across the bridge.")
            print("You discover a road leading back home.")
            print()
            print("🎉 YOU WIN! 🎉")

        if choice == "back":
            print()
            print("You turn around, but the bridge collapses!")
            print()
            print("💀 GAME OVER! 💀")


# INVALID SETTING
if setting != "mountains" and setting != "desert" and setting != "forest":

    print()
    print("❌ That is not a valid setting!")
    print("Please restart the game and choose mountains, desert or forest.")


