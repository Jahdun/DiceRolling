import random


rolls = []
count = 0

while True:
    choice = input("Roll the Dice? (y/n): ").lower()
    
    

    if choice == "y":
        faces = int(input("How many sides on your dice? "))
        dice = int(input("How many dice would you like to roll? "))
        for die in range(dice):
            dice_roll = random.randint(1, faces)
            rolls.append(dice_roll)
            count += 1
        print("You have rolled " + str(rolls))
        print(f"You have rolled the dice {count} times this session!")
    
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("invalid choice!")