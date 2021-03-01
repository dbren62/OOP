import Course_Class as c


def main():
    p = c.Course("Advanced Python", 125468, 25, MIS4322)
    d = c.Course("Database Development", 985474, 40, MIS4340)

    print(d.get_code())

    classes = {}
    classes[c.get_crn] = c.get_cap

    print(classes)


main()