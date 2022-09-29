'''
if running from the terminal type python3 dessertshop.py
'''
from abc import ABC
from packaging import Packaging

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
        cost = self.calculate_cost(self.price_per_dozen, self.cookie_quantity)
        tax = round(self.calculate_tax(cost), 2)
        receipt = f'''
{self.name}
     {self.cookie_quantity} @ ${self.price_per_dozen} dozen: ${round(cost, 2)}              [Tax: ${round(tax, 2)}]
        '''
        return receipt

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
        total = sub_total
        return total
    def __str__(self):
        cost = self.calculate_cost(self.price_per_scoop, self.scoop_count)
        tax = self.calculate_tax(cost)
        receipt = f'''
{self.name}
     {self.scoop_count} @ ${self.price_per_scoop}/scoop: ${round(cost, 2)}              [Tax: ${round(tax, 2)}]
        '''
        return receipt

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
        total = sub_total
        return total
    def __str__(self):
        cost = self.calculate_cost(self.scoop_count, self.price_per_scoop, self.topping_price)
        tax = self.calculate_tax(cost)
        reciept = f'''
{self.topping_name} {self.name} sundae
     {self.scoop_count} @ ${self.price_per_scoop}/scoop
     {self.topping_name} topping @ ${self.topping_price}: ${round(cost, 2)}          [Tax: ${round(tax, 2)}]
        '''
        return reciept

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
  
def main():
    '''
    adds some items to the order class
    '''
    customer_order = main_menu()

    order = Order()
    order.add(customer_order)

    order.items = order.items[0] # without this order.items is a list within a list

    order_subtotal = order.order_cost(order.items)
    tax_subttotal = order.order_tax(order.items)
    subtotal_sum = round(sum(order_subtotal), 2)
    tax_sum = round(sum(tax_subttotal), 2)
    
    final_total = round(subtotal_sum + tax_sum, 2)

    for item in order.items:
        print(item)
    print('------------------------------------------------------')
    print('Order Subtotals:               ${}  [Tax: ${}]'.format(subtotal_sum, tax_sum))
    print('Order total:                   ${}'.format(final_total))
    print('Total number of items in order: {}'.format(order.item_count()))

def main_menu():
    '''
    controls the main menu console interface
    '''
    menu = '''
1. Candy
2. Cookie
3. Ice cream
4. Sundae
Which would you like to add to the order? (1-4, Enter for done): 
        '''
    order = []
    while True:
        print(menu)
        item = input()
        if item == '1':
            order.append(user_prompt_candy())
        elif item == '2':
            order.append(user_prompt_cookie())
        elif item == '3':
            order.append(user_prompt_icecream())
        elif item =='4':
            order.append(user_prompt_sundae())
        else:
            return order
        
def user_prompt_candy():
    '''
    controls the candy submenu
    '''
    print('Enter type of candy:')
    candy_type = input()

    print('Enter weight of candy:')
    while True:
        try:
            candy_weight = float(input())
        except ValueError:
            print('input must be a decimal like such: 1.0, 2.7, 0.78')
            continue
        else:
            break

    print('Enter the price per pound:')
    while True:
        try:
            candy_price = float(input())
        except ValueError:
            print('input must be a decimal like such: 1.0, 2.7, 0.78')
            continue
        else:
            break
    candy_order = Candy(candy_type, candy_weight, candy_price)
    return candy_order

def user_prompt_cookie():
    '''
    controls the cookie submenu
    '''
    print('Enter type of Cookie:')
    cookie_type = input()

    print('Enter quantity purchased:')
    while True:
        try:
            cookie_number = int(input())
        except ValueError:
            print('Amount must be a whole number')
            continue
        else:
            break

    print('Enter the price per dozen:')
    while True:
        try:
            cookie_price = float(input())
        except ValueError:
            print('Input must be a decimal')
            continue
        else:
            break
    cookie_order = Cookie(cookie_type, cookie_number, cookie_price)
    return cookie_order

def user_prompt_icecream():
    '''
    controls the ice cream submenu
    '''
    print('Enter type of ice cream:')
    icecream_name = input()

    print('Enter the number of scoops')
    while True:
        try:
            scoop_number = int(input())
        except ValueError:
            print('input must be a whole number')
            continue
        else:
            break

    print('Enter ice cream price')
    while True:
        try:
            scoop_price = float(input())
        except ValueError:
            print('input must be a decimal')
            continue
        else:
            break
    icecream_order = IceCream(icecream_name, scoop_price, scoop_number)
    return icecream_order

def user_prompt_sundae():

    '''
    controls the sundae submenu
    '''
    print('Enter type of ice cream:')
    icecream_name = input()
    
    print('Enter number of scoops')
    while True:
        try:
            scoop_number = int(input())
        except ValueError:
            print('input must be a whole number')
            continue
        else:
            break
    print('Enter price per scoop')
    while True:
        try:
            scoop_price = float(input())
        except ValueError:
            print('input must be a decimal')
            continue
        else:
            break

    print('Enter topping name:')
    topping_name = input()

    print('Enter topping price:')
    while True:
        try:
            topping_price = float(input())
        except ValueError:
            print('input must be a decimal')
            continue
        else:
            break
    sundae_order = Sundae(icecream_name, scoop_number, scoop_price, topping_name, topping_price)
    return sundae_order


    order = Order()
    order.add(Candy('Candy Corn', 1.5, .25))
    order.add(Candy('Gummy Bears', .25, .35))
    order.add(Cookie('Chocolate Chip', 6, 3.99))
    order.add(IceCream('Pistachio', 2, .79))
    order.add(Sundae('Vanilla', 3, .69, 'Hot Fudge', 1.29))
    order.add(Cookie('Oatmeal Rasin', 2, 3.45))
    
    for item in order.items:
        print(item.name)
    print(f'Total number of items in order: d{order.item_count()}')

# main()
candy = Candy('Gummy Bears')
cookie = Cookie('Chocolate Chip')
print(candy)
print(cookie.get_packaging())
