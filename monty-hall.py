#!/usr/bin/env python3

# Author: undergrounder96
# Monty Hall problem, with emoji

# Emojis unicode from: https://unicode.org/emoji/charts/full-emoji-list.html
# TODO: convert the "+" from unicode to zero (3x)

# print("\U0001F914") # thinking emoji, best emoji

retries = 1

usr_choice = 99  # dummy initial value

prize = "\U0001F3CE"  # F1 car
goat = "\U0001F410"  # goat

doors = [goat, prize, goat]


def usr_choice_picker(s):
    global usr_choice

    try:
        usr_choice = int(input(f"Please select a door between [{s}]: "))
    except (Exception) as e:
        print(e.__str__())
        print()

        exit(2)


def usr_checker():
    global usr_choice, retries

    while usr_choice < 0 or usr_choice > 2:
        print(f"You have selected a wrong option: {usr_choice} !")
        print()

        usr_choice_picker("0-2")

        if retries <= 0:
            print("You ran out of retries. Good bye!")
            exit(1)

        retries -= 1


def usr_helper():
    print(f"You have picked the door: {usr_choice}...")
    print()

    if doors[usr_choice] == prize:
        # Try tricking the player
        pass

    print(f"Behind the door {usr_choice} there is: {doors[usr_choice]}")


def main():
    """This function calls all other functions"""

    usr_choice_picker("0-2")
    usr_checker()
    usr_helper()

    exit(0)


if __name__ == "__main__":
    main()
