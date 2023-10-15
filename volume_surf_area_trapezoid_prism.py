#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: October 15, 2023
# This program displays the surface area and volume of a trapezoidal prism with user input


def main():
    # get all sides of the trapezoid and the units
    print("Calculating the Surface Area and Volume of a Trapezoidal Prism")
    side_a = float(input("How long is side a (the left diagonal)?"))
    side_b = float(input("How long is side b (the long base)?"))
    side_c = float(input("How long is side c (the right diagonal)?"))
    side_d = float(input("How long is side d (the short base)"))
    length = float(input("What is the length of the prism?"))
    height = float(input("What is the height of the prism?"))
    units = str(input("What units would you like to be used (ex. cm)"))

    # calculate the surface area and volume
    surface_area = height * (side_b + side_d) + length * (
        side_a + side_b + side_c + side_d
    )
    volume = ((side_d + side_b) / 2) * height * length

    # if any of the sides <= 0, then tell the user to enter a positive number.
    if side_a <= 0:
        print("Please enter a positive number for all input options except the  units.")
    elif side_b <= 0:
        print("Please enter a positive number for all input option except the  units.")
    elif side_c <= 0:
        print("Please enter a positive number for all input options except the  units.")
    elif side_d <= 0:
        print("Please enter a positive number for all input options except the  units.")
    elif length <= 0:
        print("Please enter a positive number for all input options except the  units.")
    elif height <= 0:
        print("Please enter a positive number for all input options except the  units.")
    else:
        # otherwise, display the surface area and volume
        print("The surface area is {0} {1}^2".format(surface_area, units))
        print("The volume {0} {1}^3".format(volume, units))


if __name__ == "__main__":
    main()
