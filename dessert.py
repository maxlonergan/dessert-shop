'''
9/11/22 part one of the dessert shop
lay out all the classes with test cases in test_dessert.py
'''
from abc import ABC

class DessertItem(ABC):
    '''
    Dessert super class, all classes will extend from here
    The default name attribute should be an empty string
    '''
    def __init__(self, name=''):
        self.name = name
        self.order = []
    def calculate_cost(self):
        pass
    def calculate_tax(self, cost):
        tax = .0725
        actual_tax = cost * tax 
        return actual_tax

class Candy(DessertItem):
    '''
    candy class
    '''
    def __init__(self, name='', candy_weight=1.5, price_per_pound=2.5):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
    def calculate_cost(self, price, weight):
        # tax = super().calculate_tax(price)
        actual_price = weight / price 
        total = round(actual_price * weight, 2)
        print(total)
        

class Cookie(DessertItem):
    '''
    cookie class
    '''
    def __init__(self, name='', cookie_quantity=5, price_per_dozen=3.5):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
    def calculate_cost(self, price):
        # tax = super().calculate_tax(price)
        total = round(price, 2)
        print(total)

class IceCream(DessertItem):
    '''
    ice cream class
    '''
    def __init__(self, name='', price_per_scoop=1.75, scoop_count=4):
        super().__init__(name)
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
    def calculate_cost(self, price, scoops):
        sub_total = price * scoops
        # tax = super().calculate_tax(sub_total)
        total = round(sub_total, 2)
        print(total)

class Sundae(IceCream):
    '''
    sundae class
    '''
    def __init__(self, name='', scoop_count=4, price_per_scoop=1.75, topping_name='sprinkles', topping_price=2.5):
        super().__init__(name, price_per_scoop, scoop_count)
        self.topping_name = topping_name
        self.topping_price = topping_price
    def calculate_cost(self, scoops, scoop_price, topping_price):
        sub_total = (scoops * scoop_price) + topping_price
        # tax = super().calculate_tax(sub_total)
        total = round(sub_total, 2)
        print(total)
        

class Order():
    '''
    order class
    '''
    def __init__(self):
        self.items = DessertItem().order

    def add(self,item):
        '''
        adds an order to the item list
        '''
        self.items.append(item)

    def item_count(self):
        '''
        returns how many items are in the order list
        '''
        return len(self.items)
    def order_cost(self):
        pass


def main():
    '''
    adds some items to the order class
    '''
    order = Order()
    order.add(Candy('Candy Corn', 1.5, .25))
    order.add(Candy('Gummy Bears', .25, .35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, 7.99))
    order.add(Sundae('Vanilla', 3, .69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Raisin', 2, 3.45))

    for item in order.items:
        print(item.name)

    print(f'Total number of items in order: {order.item_count()}')

# candy = Candy()
# cookie = Cookie()
# ice_cream = IceCream()
# sundae = Sundae()

# candy.calculate_cost(candy.price_per_pound, candy.candy_weight)
# cookie.calculate_cost(cookie.price_per_dozen)
# ice_cream.calculate_cost(ice_cream.price_per_scoop, ice_cream.scoop_count)
# sundae.calculate_cost(sundae.scoop_count, sundae.price_per_scoop, sundae.topping_price)
