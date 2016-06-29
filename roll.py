import random
import sys

def roll_dice(dice_sides):
    while True:
        user_input = input("Would you like to role the dice? (yes/no) ")
        if user_input in ['yes', 'Yes', 'y', 'no', 'No', 'n']:
            break;
        else:
            print("This is not a valid option. Would you like to role the dice? (yes/no)")
    if user_input in ['yes', 'Yes', 'y']:
        dice_roll = random.randint(1,dice_sides)
        return dice_roll
    elif user_input in ['no', 'No', 'n']:
        print("Ok no roll will take place")


dice_sides = int(input("What side dice do you wish to use? "))
result = roll_dice(dice_sides)
print(result) 
