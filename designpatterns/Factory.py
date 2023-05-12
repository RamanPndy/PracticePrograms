class Burger:
    def __init__(self, ingrediants) -> None:
        self.ingrediants = ingrediants

class BurgerFactory:
    def createCheeseBurger(self):
        ingrediants = ["bun", "cheese"]
        return Burger(ingrediants)
    
    def createDeluxCheeseBurger(self):
        ingrediants = ["bun", "cheese", "tomato", "lettuce"]
        return Burger(ingrediants)
    
    def createVeganBurger(self):
        ingrediants = ["bun", "sauce", "veggie-patty"]
        return Burger(ingrediants)
    
burgerFactory = BurgerFactory()
burgerFactory.createCheeseBurger()
burgerFactory.createVeganBurger()