# Created by Dylan Melo
# Created on December 2021
# This program asks the user for the unit, height, base
# and all side lengths of the triangle. It then
# calculates and displays the area and
# perimeter.
import math
import colorama
from colorama import Fore
from colorama import Style


def main():
    # input
    colorama.init()
    print(Fore.BLUE + Style.BRIGHT + "Today we will calculate the area and")
    print(Fore.GREEN + Style.BRIGHT + "perimeter of a triangle")
    unit = str(input(Fore.CYAN + Style.BRIGHT + "Enter the unit: "))
    height = float(input(Fore.RED + Style.BRIGHT + "Enter the height: "))
    base = float(input(Fore.MAGENTA + "Enter the base: "))
    side_a = float(input(Fore.BLUE + "Enter the side a length: "))
    side_b = float(input(Fore.CYAN + Style.DIM + "Enter the side b length: "))
    side_c = float(input(Fore.RED + "Enter the side c length: "))

    # process
    area = height*base/2
    perimeter = side_a + side_b + side_c

    # output
    print("")
    print(Fore.BLUE + Style.BRIGHT + "Area = {:,.2f} {}^2". format(area, unit))
    print(Fore.CYAN + "Perimeter = {:,.2f} {}". format(perimeter, unit))


if __name__ == "__main__":
    main()
