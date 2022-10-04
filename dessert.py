'''
if running from the terminal type python3 dessertshop.py
This module contains the dessert class heirarchy except for the classes
contained in packaging.py
'''
from abc import ABC
from cgi import test
from packaging import Packaging
from payment import *

class DessertItem(Packaging, ABC):
    '''
    Dessert super class, all classes will extend from here
    The default name attribute should be an empty string
    '''
    tax_percent = 7.25
    def __init__(self, name=''):
        self.name = name
        self.order = []
    def calculate_cost(self):
        pass
    def calculate_tax(self, cost):
        tax = .0725
        actual_tax = cost * tax
        return actual_tax
    def get_packaging(self):
        '''
        returns what is used to package the item
        '''
        return self.package_type
    def set_packaging(self, package):
        '''
        sets what should be used to package the item
        '''
        self.package_type = package

class Candy(DessertItem):
    '''
    candy class
    constructor (name, candy_weight, price_per_pound)
    '''
    def __init__(self, name='', candy_weight=1.50, price_per_pound=2.50):
        super().__init__(name)
        super().set_packaging('Bag')
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
    def calculate_cost(self, price, weight):
        return price * weight
    def __str__(self):
        package = super().get_packaging()
        cost = self.calculate_cost(self.price_per_pound, self.candy_weight)
        tax = round(self.calculate_tax(cost), 2)
        receipt = f'''
{self.name}  ({package})
     {self.candy_weight} @ ${self.price_per_pound}/lb: ${round(cost, 2)}               [Tax: ${round(tax, 2)}]
        '''
        return receipt

class Cookie(DessertItem):
    '''
    cookie class
    constructor (name, cookie_quantity, price_per_dozen)
    '''
    def __init__(self, name='', cookie_quantity=5, price_per_dozen=3.5):
        super().__init__(name)
        super().set_packaging('Box')
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
    def calculate_cost(self, price, amount):
        # tax = super().calculate_tax(price)
        ratio = price / 12
        return ratio * amount
    def __str__(self):
        package = super().get_packaging()
        cost = self.calculate_cost(self.price_per_dozen, self.cookie_quantity)
        tax = round(self.calculate_tax(cost), 2)
        receipt = f'''
{self.name}  ({package})
     {self.cookie_quantity} @ ${self.price_per_dozen} dozen: ${round(cost, 2)}              [Tax: ${round(tax, 2)}]
        '''
        return receipt

class IceCream(DessertItem):
    '''
    ice cream class
    constructor (name, price_per_scoop, scoop_count)
    '''
    def __init__(self, name='', price_per_scoop=1.75, scoop_count=4):
        super().__init__(name)
        super().set_packaging('Bowl')
        self.scoop_count = scoop_count
        self.price_per_scoop = price_per_scoop
    def calculate_cost(self, price, scoops):
        sub_total = price * scoops
        total = sub_total
        return total
    def __str__(self):
        package = super().get_packaging()
        cost = self.calculate_cost(self.price_per_scoop, self.scoop_count)
        tax = self.calculate_tax(cost)
        receipt = f'''
{self.name}  ({package})
     {self.scoop_count} @ ${self.price_per_scoop}/scoop: ${round(cost, 2)}              [Tax: ${round(tax, 2)}]
        '''
        return receipt

class Sundae(IceCream):
    '''
    sundae class
    constructor (name, scoop_count, price_per_scoop, topping_name, topping_price)
    '''
    def __init__(self, name='', scoop_count=4, price_per_scoop=1.75, topping_name='sprinkles', topping_price=2.5):
        super().__init__(name, price_per_scoop, scoop_count)
        super().set_packaging('Boat')
        self.topping_name = topping_name
        self.topping_price = topping_price
    def calculate_cost(self, scoops, scoop_price, topping_price):
        sub_total = (scoops * scoop_price) + topping_price
        total = sub_total
        return total
    def __str__(self):
        package = super().get_packaging()
        cost = self.calculate_cost(self.scoop_count, self.price_per_scoop, self.topping_price)
        tax = self.calculate_tax(cost)
        reciept = f'''
{self.topping_name} {self.name} sundae  ({package})
     {self.scoop_count} @ ${self.price_per_scoop}/scoop
     {self.topping_name} topping @ ${self.topping_price}: ${round(cost, 2)}          [Tax: ${round(tax, 2)}]
        '''
        return reciept

class Order(Payment):
    '''
    order class
    '''

    def __init__(self):
        self.items = DessertItem().order
        self.pay_method = Payment().pay_type
        self.counter = 1

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

    def order_cost(self, item_list):
        '''
        adds up the subtotal of the order before tax
        should probably rework to be closer to order_tax
        '''
        count = []
        for item in item_list:
            if isinstance(item, Candy) == True:
                count.append(item.calculate_cost(item.price_per_pound, item.candy_weight))
            elif isinstance(item, Cookie) == True:
                count.append(item.calculate_cost(item.price_per_dozen, item.cookie_quantity))
            elif isinstance(item, Sundae) == True:
                count.append(item.calculate_cost(item.scoop_count, item.price_per_scoop, item.topping_price))
            elif isinstance(item, IceCream) == True:
                count.append(item.calculate_cost(item.price_per_scoop, item.scoop_count))
        return count
        
    
    def order_tax(self, item_list):
        '''
        returns the tax as a list of the tax of each item
        '''
        tax_count = []
        for item in item_list:
            if isinstance(item, Candy) == True:
                cost = item.calculate_cost(item.price_per_pound, item.candy_weight)
                tax_count.append(item.calculate_tax(cost))
            elif isinstance(item, Cookie) == True:
                cost = item.calculate_cost(item.price_per_dozen, item.cookie_quantity)
                tax_count.append(item.calculate_tax(cost))
            elif isinstance(item, Sundae) == True:
                cost = item.calculate_cost(item.price_per_scoop, item.scoop_count, item.topping_price)
                tax_count.append(item.calculate_tax(cost))
            elif isinstance(item, IceCream) == True:
                cost = item.calculate_cost(item.price_per_scoop, item.scoop_count)
                tax_count.append(item.calculate_tax(cost))
        return tax_count

    def payment_method(self, new_payment):
        '''
        returns the payment method
        '''
        payment = Payment()
        payment.pay_type = new_payment
        return payment.pay_type

    def __str__(self):
        order = Order()
        payment = order.payment_method(self.counter)
        receipt = (f'Paid with {payment}')
        return receipt

