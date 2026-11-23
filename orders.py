class Pizza:
    SIZES = ("Small", "Medium", "Large", "Extra-large")

    def __init__(self, toppings, size="Large"):
        self.toppings = toppings
        if size in self.SIZES:
            self.__size = size
        else:
            self.__size = "Large"

    def get_size(self):
        return self.__size