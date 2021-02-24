class CellPhone:
    def __init__(self):
        self.__manufact = ""
        self.__model = ""
        self.__retail_price = 0

    def set_manufact(self):
        self.__manufact = input("Enter manufacturer: ")

    def set_model(self):
        self.__model = input("Enter model number: ")

    def set_retail_price(self):
        self.__retail_price = input("Enter suggested retail price: ")

    def get_manufact(self):
        return self.__manufact

    def get_model(self):
        return self.__model

    def get_retail_price(self):
        return self.__retail_price
