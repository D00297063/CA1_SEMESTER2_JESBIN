##create the pizza class
class Pizza:
    CorrectSize = ["_small", "_Medium", "_Large", "_Extra-Large"]
    Topping = ["_Tomato", "_Onion", "_Sweetcorn", "_Bacon"]




##add the main consructor here
def __init__(self, Topping, CorrectSize = "Large"):

    self.Topping = Topping

    if CorrectSize in self.CorrectSize:
        self.__CorrectSize = CorrectSize

    else:
        self.__CorrectSize = "Large"


##call for the size
def get_size(self):
      return self.__CorrectSize      
