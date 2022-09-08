class DessertItem:
    '''
    Dessert super class, all classes will extend from here
    The default name attribute should be an empty string
    '''
    def __init__(self,name=''):
        self.name = name

class Candy(DessertItem):
    def __init__(self, candy_weight=1.5, price_per_pound=2.5, name=''):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound

class Cookie(DessertItem):
    def __init__(self, cookie_quantity=5, price_per_dozen=3.5, name=''):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen

class IceCream(DessertItem):
    def __init__(self, scoop_count=4, price_per_scoop=1.75, name=''):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop

class Sudae(IceCream):
    def __init__(self, scoop_count, price_per_scoop, topping_name, topping_price, name=''):
        super().__init__(scoop_count, price_per_scoop, name)
        self.topping_name = topping_name
        self.topping_price = topping_price


candy = Candy()

print('haha it works')