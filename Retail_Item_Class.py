class Retail_Item:
    def __init__(self, desc, quantity, price):
        self.__item_description = desc
        self.__quantity = quantity
        self.__price = price

    def __str__(self):
        return (
            "Description: "
            + str(self.__item_description)
            + "\n"
            + "Quantity: "
            + str(self.__quantity)
            + "\n"
            + "Price: "
            + str(self.__price)
        )