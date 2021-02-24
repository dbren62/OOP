import Cell_Phone_Class as iPhone


def main():
    my_phone = iPhone.CellPhone()

    my_phone.set_manufact()
    my_phone.set_model()
    my_phone.set_retail_price()

    print("Manufacturer: ", my_phone.get_manufact())
    print("Model: ", my_phone.get_model())
    print("Retail Price: $", my_phone.get_retail_price())


main()