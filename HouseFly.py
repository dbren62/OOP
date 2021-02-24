import InsectClass as HouseFly


def main():

    this_fly = HouseFly.Insect(4, 8, 0)
    print(this_fly)
    print("This insect can fly", this_fly.flight_distance(), "miles")


"""
    print(this_fly.legs, "legs")
    print(this_fly.wings, "wings")
"""


main()