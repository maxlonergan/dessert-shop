'''
This module handles everything dealing with the input and output of the program
'''

from dessert import DessertItem
from packaging import Packaging

from dessert import Candy
from dessert import Cookie
from dessert import IceCream
from dessert import Sundae
from dessert import Order


class Customer():
    '''
    customer class
    '''
    next_customer_id: int = 0
    def __init__(self, name) -> None:
        self.customer_name: str = name
        self.order_history: list[Order] = []
        self.customer_id: int = 1

    def add2history(self,order:Order):
        self.order_history.append(order)
        return self

customer_db: dict[str,Customer] = {
    'John':Customer('John')
}
customer_db['John'].customer_id = 1000

def main():
    '''
    adds some items to the order class
    '''
    customer_order = main_menu()
    order = Order()
    order.add(customer_order) # adds whatever is ordered into a list
    order_count = len(order.items)

    # all the math for the prices happens in this chunk
    order_subtotal = order.order_cost(order.items)
    tax_subttotal = order.order_tax(order.items)
    subtotal_sum = round(sum(order_subtotal), 2)
    tax_sum = round(sum(tax_subttotal), 2)
    final_total = round(subtotal_sum + tax_sum, 2)

    order.items.sort() # sorts items from cheapest to most expensive

    print('Enter the customer name:')
    cust_name = str(input())
    check_database(customer_db, cust_name)
    print(customer_db)
    quit()
    # order.counter keeps track of which payment option was picked from the terminal
    order.counter = payment_options()

    # everything below is in charge of printing the reciept
    print('----------------------Receipt-------------------------')
    for item in order.items:
        print(item)
    print('------------------------------------------------------')
    print('Order Subtotals:               ${}  [Tax: ${}]'.format(subtotal_sum, tax_sum))
    print('Order total:                   ${}'.format(final_total))
    print('Total number of items in order: {}'.format(order_count))
    print('------------------------------------------------------')
    print(order)
    print('press y and enter to place another order')
    answer = input()
    if answer == 'y':
        main()
    else:
        quit()


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

def payment_options():
    '''
    controls the payment options part of the dessert shop
    '''
    payment_options = '''
1. Cash
2. Card
3. Phone
Enter payment method:
    '''
    payment_choice = 0
    while True:
        print(payment_options)
        item = input()
        if item == '1':
            payment_choice = 1
            return payment_choice
        elif item == '2':
            payment_choice = 2
            return payment_choice
        elif item == '3':
            payment_choice = 3
            return payment_choice

def check_database(db, name):
    '''
    checks if a name is in the customer database
    if the name isn't in the database the name gets added
    '''
    if name in db:
        print('thats already a customer silly')
    else:
        db.update({name:Customer(name)})

main()

