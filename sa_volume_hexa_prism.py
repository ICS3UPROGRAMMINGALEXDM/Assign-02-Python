#!/usr/bin/env python3

# Created By: Alex De Meo
# Date: 03/27/2022
# Description: This program calculates the surface area and volume
# of a hexagonal prism with user input
import math

import colorama
from colorama import Back, Fore, Style


# introduction fnctn gives the opening sentence
def introduction():
    print(
        "This program calculates the Volume and Surface Area of a regular \nhexagonal prism. \n\n"
    )


# fnctn is called to select the units
def unitselect():
    introduction()

    while True:
        # getting user input for the unit
        unitselect.unit = (
            input("Please enter the unit of measurement (cm, m, in, mm)\n")
            .strip()
            .lower()
        )

        # checking the unit to ensure it is one recognizable to the progtram
        if (
            (unitselect.unit == "mm")
            or (unitselect.unit == "cm")
            or (unitselect.unit == "m")
            or (unitselect.unit == "in")
        ):
            print("Unit selected successfully!")
            break
        else:
            print(
                "I don't recognize that unit. Please try again with one of the following (cm, m, in, mm)"
            )


# Function for calculations
def calculate():
    unitselect()
    # while loop for error checking the the user input for length
    while True:
        # get length
        num = input("Please enter the base length of your hexagonal prism \n").strip()
        try:
            length = float(num)
            # Checks to ensure the number entered is positive
            if length > 0:
                break
            else:
                print("Can not be a negative number.")
        except ValueError:
            print("This number is invalid. Please try again.")
    # while loop for error checking the the user input for height
    while True:
        # get height
        num2 = input("Please enter the height of your hexagonal prism\n")
        try:
            height = float(num2)
            if height > 0:
                break
            else:
                print("Can not be a negative number.")
        except ValueError:
            print("That number is not valid. Please try again.")

    # Calculations for surface area and volume
    calculate.area = (6 * length * height) + (3 * math.sqrt(3)) * (length**2)
    calculate.volume = (3 * math.sqrt(3)) / 2 * (length**2) * height


# function is for displaying results
def final_statements():
    calculate()

    # Display syntax' for surface area and volume
    print(
        Fore.YELLOW
        + Style.BRIGHT
        + "The surface area of your hexagon is {:.2f} {}^2".format(
            calculate.area, unitselect.unit
        )
    )

    print(
        "The volume of your hexagon is {:.2f} {}^3".format(
            calculate.volume, unitselect.unit
        )
    )


def main():
    final_statements()


if __name__ == "__main__":
    main()
