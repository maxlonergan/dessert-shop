'''
if running from the terminal type python3 dessertshop.py
'''
from abc import ABC

class DessertItem(ABC):
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

class Candy(DessertItem):
    '''
    candy class
    '''
    def __init__(self, name='', candy_weight=1.5, price_per_pound=2.5):
        super().__init__(name)
        self.candy_weight = candy_weight
        self.price_per_pound = price_per_pound
    def calculate_cost(self, price, weight):
        return price * weight
        
class Cookie(DessertItem):
    '''
    cookie class
    '''
    def __init__(self, name='', cookie_quantity=5, price_per_dozen=3.5):
        super().__init__(name)
        self.cookie_quantity = cookie_quantity
        self.price_per_dozen = price_per_dozen
    def calculate_cost(self, price, amount):
        # tax = super().calculate_tax(price)
        ratio = price / 12
        return ratio * amount

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
    order = Order()
    candy_one = Candy('Candy Corn', 1.5, .25)
    candy_two = Candy('Gummy Bears', .25, .35)
    cookie = Cookie('Chocolate Chip', 6, 3.99)
    ice_cream = IceCream('Pistachio', 2, .79)
    sundae = Sundae('Vanilla', 3, .69, 'Hot Fudge', 1.29)
    cookie_two = Cookie('Oatmeal Raisin', 2, 3.45)

    order.add(candy_one)
    order.add(candy_two)
    order.add(cookie)
    order.add(ice_cream)
    order.add(sundae)
    order.add(cookie_two)

    # order.order_cost(order.items)
    # order.order_tax(order.items)
    order_subtotal = order.order_cost(order.items)
    tax_subttotal = order.order_tax(order.items)
    subtotal_sum = round(sum(order_subtotal), 2)
    tax_sum = round(sum(tax_subttotal), 2)
    
    final_total = round(subtotal_sum + tax_sum, 2)

    i = 0
    for item in order.items:
        # print(f'{item.name}:      ${round(order_subtotal[i], 2)}    [Tax: ${round(tax_subttotal[i], 2)}]')
        print('{:<30} ${:<5} [Tax: ${}]'.format((item.name + ':'), round(order_subtotal[i], 2), round(tax_subttotal[i], 2)))
        i += 1
    print('------------------------------------------------------')
    print('Order Subtotals:               ${}  [Tax: ${}]'.format(subtotal_sum, tax_sum))
    print('Order total:                   ${}'.format(final_total))
    print('Total number of items in order: {}'.format(order.item_count()))

def validate_float(user_input):
    '''
    validates input and if correct returns the input as a float
    '''
    while True:
        try:
            flo = float(user_input)
            yield flo
        except ValueError:
            print('input must be a decimal like such: 1.0, 2.7, 0.78')
            continue
        else:
            break

def main_menu():
    menu = '''
1. Candy
2. Cookie
3. Ice cream
4. Sundae
Which would you like to add to the order? (1-4, Enter for done): 
        '''
    print(menu)
    item = input()
    if item == '1':
        # add code below to user_prompt_candy and instead call user_prompt_candy()
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

    elif item == '2':
        user_prompt_cookie()
        # print('Enter type of Cookie')
        # cookie_order = input()
    elif item == '3':
        print('gross....ice cream')
    elif item =='4':
        print('sundaeeeeeee')
    else:
        print('pick one of the options dammit')

def user_prompt_candy():
    pass

def user_prompt_cookie():
    print('Enter type of Cookie:')
    cookie_order = input()
    print('Enter quantity purchased:')
    cookie_number = input()
    print('Enter the price per dozen:')
    cookie_price = input()

def user_prompt_icecream():
    pass

def user_prompt_sundae():
    pass

# main()
# main_menu()
validate_float('test')


