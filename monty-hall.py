#!/usr/bin/env python3

# Author: undergrounder96
# Monty Hall problem, with emoji

from time import sleep
from random import randint

# Emojis unicode from: https://unicode.org/emoji/charts/full-emoji-list.html
# TODO: convert the "+" from unicode to zero (3x)

# print("\U0001F914") # thinking emoji, best emoji


usr_choice = 99  # dummy initial value

prize = "\U0001F3CE"  # F1 car
goat = "\U0001F410"  # goat

doors = {key: goat for key in range(0, 3)}


def randomize_prize():
    global doors

    tmp = len(doors) - 1

    doors[randint(0, tmp)] = prize

    # for debugging only :)
    # print(f"doors = {doors}")


def usr_choice_picker():
    global usr_choice

    print()

    try:
        usr_choice = int(input(f"Please select a door {list(doors.keys())}: "))
    except (Exception) as e:
        print(e.__str__())
        print()

        exit(2)


def usr_helper():
    global usr_choice

    print(f"You have picked the door: {usr_choice}...")
    print()

    for trick_usr in range(0, 3):
        if trick_usr != usr_choice and doors[trick_usr] == goat:
            print(
                f"Behind the door {trick_usr} there is: {doors.pop(trick_usr)}")

            print("Would you like to change doors?")

            if str(input("[y/n]: ")).lower() == "y":
                usr_choice_picker()
            else:
                print("Assuming no changes...")

            print("Unveiling...")
            sleep(0.7)

            print(
                f"\nBehind the door {usr_choice} there is: {doors[usr_choice]}\n")

            if doors[usr_choice] == prize:
                print("Congratulations. You won the prize!!!")

            else:
                print(f"Better luck next time. You have lost the {prize}")

            break


def main():
    """This function calls all other functions"""

    randomize_prize()

    usr_choice_picker()
    usr_helper()

    exit(0)


if __name__ == "__main__":
    main()
