import Car_Class as c


def main():
    carOne = c.Car("2016 F-150", "Ford")

    print("Accelerating...")
    for i in range(5):
        carOne.accelerate()
        print(carOne.get_speed())

    print("Hit the brake...")
    for i in range(5):
        carOne.brake()
        print(carOne.get_speed())


main()