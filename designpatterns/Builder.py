class Burger:
    def __init__(self) -> None:
        self.buns = None
        self.patty = None
        self.cheese = None
    
    def setBuns(self, buns):
        self.buns = buns
    
    def setPatty(self, patty):
        self.patty = patty
    
    def setCheese(self, cheese):
        self.cheese = cheese

class BurgerBuilder:
    def __init__(self) -> None:
        self.burger = Burger()

    def addBuns(self, buns):
        self.burger.setBuns(buns)
        return self
    
    def addPatties(self, patty):
        self.burger.setPatty(patty)
        return self
    
    def addCheese(self, cheese):
        self.burger.setCheese(cheese)
        return self
    
    def build(self):
        return self.burger
    
burger = BurgerBuilder().addBuns("sesame").addCheese("swiss cheese").addPatties("veg-patty").build()