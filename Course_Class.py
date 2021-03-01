class Course:
    def __init__(self, title, crn, cap, code):
        self.__title = title
        self.__crn = 0
        self.__cap = 0
        self.__code = code

    def get_title(self):
        return self.__title

    def get_crn(self):
        return self.__crn

    def get_cap(self):
        return self.__cap

    def get_code(self):
        return self.__code