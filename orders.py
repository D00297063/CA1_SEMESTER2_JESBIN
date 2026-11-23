class Pizza:
    SIZES = ("Small", "Medium", "Large", "Extra-large")
    __size = "Large"

    def __init__(self):
        self.toppings = []

    def get_size(self):
        return self.__size