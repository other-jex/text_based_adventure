print("Welcome to the Adventure Game!")
print("Your mission is to find the hidden treasure.\n")


choice1 = input(
    "You are at a crossroad. Do you want to go 'left' or 'right'? ").lower()

if choice1 == "left":
    choice2 = input(
        "You encounter a river. Do you 'swim' across or 'wait' for a boat? ").lower()
    if choice2 == "swim":
        print("You were eaten by a crocodile! Game Over. ❌")
    elif choice2 == "wait":
        choice3 = input(
            "You safely crossed. You see a cave. Do you enter it? 'yes' or 'no'? ").lower()
        if choice3 == "yes":
            print("Congratulations! You found the hidden treasure! 🏆")
        else:
            print("You missed the treasure. Game Over. ❌")

    else:
        print("Invalid choice. Game Over. ❌")

elif choice1 == "right":
    print("You walked into a trap! Game Over. ❌")
else:
    print("Invalid choice. Game Over. ❌")
