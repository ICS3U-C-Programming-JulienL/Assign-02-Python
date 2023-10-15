#!/usr/bin/env python3

# Created By: Julien Lamoureux
# Date: October 15, 2023
# This program displays the surface area and volume of a trapezoidal prism with user input


def main():
    # get all sides of the trapezoid and the units
    print("Calculating the Surface Area and Volume of a Trapezoidal Prism")
    side_a = float(input("How long is side a (the left diagonal): "))
    side_b = float(input("How long is side b (the base on the bottom): "))
    side_c = float(input("How long is side c (the right diagonal): "))
    side_d = float(input("How long is side d (the base on the top): "))
    length = float(input("What is the length of the prism: "))
    height = float(input("What is the height of the prism: "))
    units = str(input("What units would you like to be used (ex. cm): "))

    # calculate the surface area and volume
    surface_area = height * (side_b + side_d) + length * (
        side_a + side_b + side_c + side_d
    )
    volume = ((side_d + side_b) / 2) * height * length

    # if any of the sides <= 0, then tell the user to enter a positive number.
    if side_a <= 0:
        print("Please enter a positive number for side a.")
    elif side_b <= 0:
        print("Please enter a positive number for side b.")
    elif side_c <= 0:
        print("Please enter a positive number for side c.")
    elif side_d <= 0:
        print("Please enter a positive number for side d.")
    elif length <= 0:
        print("Please enter a positive number for the length.")
    elif height <= 0:
        print("Please enter a positive number for the height.")
    else:
        # otherwise, display the surface area and volume
        print("The surface area is {0:.2f} {1}^2.".format(surface_area, units))
        print("The volume is {0:.2f} {1}^3.".format(volume, units))


if __name__ == "__main__":
    main()
