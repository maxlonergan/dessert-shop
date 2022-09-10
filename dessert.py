'''
9/11/22 part one of the dessert shop
lay out all the classes with test cases in test_dessert.py
'''

class DessertItem:
    '''
    Dessert super class, all classes will extend from here
    The default name attribute should be an empty string
    '''
    def __init__(self, name=''):
        self.name = name

class Candy(DessertItem):
    def __init__(self, name='', candy_weight=1.5, price_per_pound=2.5):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

class Cookie(DessertItem):
    def __init__(self, name='', cookie_quantity=5, price_per_dozen=3.5):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

class IceCream(DessertItem):
    def __init__(self, name='', price_per_scoop=1.75, scoop_count=4):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

class Sundae(IceCream):
    def __init__(self, name='', price_per_scoop=1.75, topping_name='sprinkles', topping_price=2.5):
        super().__init__(name, price_per_scoop)
        self.topping_name = topping_name
        self.topping_price = topping_price



candy = Candy()
# sundae.price_per_scoop = 2.5

print(candy.name)