'''
test cases for dessert.py
to test type: python3 -m pytest test_dessert.py into the terminal
'''

# maybe add some isinstance(x, int)
# isinstance() can be set to check if a variable is a certain data type like int or str

from dessert import *
from packaging import Packaging
from payment import Payment

# to test type: python3 -m pytest test_dessert.py into the terminal

def test_default():
    '''
    tests default values following this order
    1. Call the constructor with default values
    2. Test each attribute for its expected default value
    '''
    candy = Candy()
    assert candy.candy_weight == 1.5
    assert candy.price_per_pound == 2.5
    assert candy.name == ''

    cookie = Cookie()
    assert cookie.cookie_quantity == 5
    assert cookie.price_per_dozen == 3.5
    assert cookie.name == ''

    ice_cream = IceCream()
    assert ice_cream.scoop_count == 4
    assert ice_cream.price_per_scoop == 1.75
    assert ice_cream.name == ''

    sundae = Sundae()
    assert sundae.topping_name == 'sprinkles'
    assert sundae.topping_price == 2.5
    assert sundae.price_per_scoop == 1.75
    assert sundae.name == ''
    assert sundae.scoop_count == 4

def test_alternate():
    '''
    tests alternate values of each method following this order
    3. Call the constructor with non-default values
    4. Test each attribute for its expected value
    '''
    candy = Candy('peppermint',2.5,5.0,)
    assert candy.candy_weight == 2.5
    assert candy.price_per_pound == 5.0
    assert candy.name == 'peppermint'

    cookie = Cookie('chocolate chip',12,6.5)
    assert cookie.cookie_quantity == 12
    assert cookie.price_per_dozen == 6.5
    assert cookie.name == 'chocolate chip'

    ice_cream = IceCream('vanilla',2.5,6)
    assert ice_cream.scoop_count == 6
    assert ice_cream.price_per_scoop == 2.5
    assert ice_cream.name == 'vanilla'

    sundae = Sundae('test sundae', 3 ,1.50,'chocolate',4.0)
    assert sundae.name == 'test sundae'
    assert sundae.scoop_count == 3
    assert sundae.price_per_scoop == 1.50
    assert sundae.topping_name == 'chocolate'
    assert sundae.topping_price == 4.0

# tests with _modify_ should be following this guide
# 1. Call the constructor with default values
# 2. Modify an attribute
# 3. Test the attribute to see that it has its new value
# 4. Repeat steps 2 and 3 for each attribute
# 5. Call the constructor with non-default values
# 6. Modify an attribute
# 7. Test the attribute to see that it has its new value
# 8. Repeat steps 6 and 7 for each attribute

def test_modify_candy():
    '''
    tests methods after modifying values of attributes of the Candy class
    '''
    candy = Candy()
    candy.name = 'caramel'
    assert candy.name == 'caramel'
    candy.candy_weight = 3.0
    assert candy.candy_weight == 3.0
    candy.price_per_pound = 6.0
    assert candy.price_per_pound == 6.0

    candy = Candy(3.0,4.0,'sucker')
    candy.name = 'gum'
    assert candy.name == 'gum'
    candy.candy_weight = 1.0
    assert candy.candy_weight == 1.0
    candy.price_per_pound = 10.0
    assert candy.price_per_pound == 10.0

def test_modify_cookie():
    '''
    tests methods after modifying values of attributes of the Cookie class
    '''
    cookie = Cookie()
    cookie.name = 'macadamia'
    assert cookie.name == 'macadamia'
    cookie.cookie_quantity = 20
    assert cookie.cookie_quantity == 20
    cookie.price_per_dozen = 12.5
    assert cookie.price_per_dozen == 12.5

    cookie = Cookie(12,5.5,'peanut')
    cookie.name = 'chocolate'
    assert cookie.name == 'chocolate'
    cookie.cookie_quantity = 5
    assert cookie.cookie_quantity == 5
    cookie.price_per_dozen = 1.5
    assert cookie.price_per_dozen == 1.5

def test_modify_ice_cream():
    '''
    tests methods after modifying values of attributes of the IceCream class
    '''
    ice_cream = IceCream()
    ice_cream.name = 'strawberry'
    assert ice_cream.name == 'strawberry'
    ice_cream.scoop_count = 1
    assert ice_cream.scoop_count == 1
    ice_cream.price_per_scoop = 0.5
    assert ice_cream.price_per_scoop == 0.5

    ice_cream = IceCream('vanilla',6.5,3)
    ice_cream.name = 'chocolate'
    assert ice_cream.name == 'chocolate'
    ice_cream.scoop_count = 1
    assert ice_cream.scoop_count == 1
    ice_cream.price_per_scoop = 1.5
    assert ice_cream.price_per_scoop == 1.5

def test_modify_sundae():

    '''
    tests methods after modifying calues of attributes of the Sundae class
    '''

    sundae = Sundae()
    sundae.name = 'candy'
    assert sundae.name == 'candy'
    sundae.scoop_count = 1
    assert sundae.scoop_count == 1
    sundae.topping_name = 'test name'
    assert sundae.topping_name == 'test name'
    sundae.topping_price = 4.0
    assert sundae.topping_price == 4.0
    sundae.price_per_scoop = .5
    assert sundae.price_per_scoop == .5

    sundae = Sundae('peanuts',3, 1.5, 'test name', 4.75)
    sundae.name = 'chocolate'
    assert sundae.name == 'chocolate'
    sundae.scoop_count = 6
    assert sundae.scoop_count == 6
    sundae.price_per_scoop = 2.75
    assert sundae.price_per_scoop == 2.75
    sundae.topping_name = 'candy'
    assert sundae.topping_name == 'candy'
    sundae.topping_price = 6.75
    assert sundae.topping_price == 6.75

def test_tax_attribute():
    candy = Candy()
    assert candy.tax_percent == 7.25

def test_calculate_cost():
    '''
    tests the method calculate_cost()
    '''
    candy = Candy()
    assert candy.calculate_cost(candy.candy_weight, candy.price_per_pound) == 3.75
    cookie = Cookie()
    assert round(cookie.calculate_cost(cookie.price_per_dozen, cookie.cookie_quantity), 2) == 1.46
    ice_cream = IceCream()
    assert ice_cream.calculate_cost(ice_cream.price_per_scoop, ice_cream.scoop_count) == 7
    sundae = Sundae()
    assert sundae.calculate_cost(sundae.scoop_count, sundae.price_per_scoop, sundae.topping_price) == 9.5

def test_calculate_tax():
    '''
    tests the method calculate_tax()
    '''
    candy = Candy()
    candy_cost = candy.calculate_cost(candy.candy_weight, candy.price_per_pound)
    candy_tax = candy.calculate_tax(candy_cost)
    assert candy.calculate_tax(candy_cost) == candy_tax
    cookie = Cookie()
    cookie_cost = cookie.calculate_cost(cookie.price_per_dozen, cookie.cookie_quantity)
    cookie_tax = cookie.calculate_tax(cookie.calculate_cost(cookie.price_per_dozen, cookie.cookie_quantity))
    assert cookie.calculate_tax(cookie_cost) == cookie_tax
    ice_cream = IceCream()
    ice_cream_cost = ice_cream.calculate_cost(ice_cream.price_per_scoop, ice_cream.scoop_count)
    ice_cream_tax = ice_cream.calculate_tax(ice_cream.calculate_cost(ice_cream.price_per_scoop, ice_cream.scoop_count))
    assert ice_cream.calculate_tax(ice_cream_cost) == ice_cream_tax
    sundae = Sundae()
    sundae_cost = sundae.calculate_cost(sundae.scoop_count, sundae.price_per_scoop, sundae.topping_price)
    sundae_tax = sundae.calculate_tax(sundae.calculate_cost(sundae.scoop_count, sundae.price_per_scoop, sundae.topping_price))
    assert sundae.calculate_tax(sundae_cost) == sundae_tax

def test_packaging():
    candy = Candy()
    assert candy.get_packaging() == 'Bag'
    cookie = Cookie()
    assert cookie.get_packaging() == 'Box'
    icecream = IceCream()
    assert icecream.get_packaging() == 'Bowl'
    sundae = Sundae()
    assert sundae.get_packaging() == 'Boat'

def test_payment():
    test_order = Order()
    assert test_order.payment_method(1) == 'CASH'
    assert test_order.payment_method(2) == 'CARD'
    assert test_order.payment_method(3) == 'PHONE'

def test_equal():
    candy = Candy()
    test_candy = Candy()
    candy.calculate_cost(1.5,1.5)
    test_candy.calculate_cost(1.5,1.5)
    assert candy == test_candy
    cookie = Cookie()
    test_cookie = Cookie()
    cookie.calculate_cost(4.99, 12)
    test_cookie.calculate_cost(4.99, 12)
    assert cookie == test_cookie
    icecream = IceCream()
    test_icecream = IceCream()
    icecream.calculate_cost(1.75,6)
    test_icecream.calculate_cost(1.75,6)
    assert icecream == test_icecream
    sundae = Sundae()
    test_sundae = Sundae()
    sundae.calculate_cost(4, 1.75, 1.50)
    test_sundae.calculate_cost(4, 1.75, 1.50)
    assert sundae == test_sundae

def test_lt():
    candy = Candy()
    test_candy = Candy()
    candy.calculate_cost(1.75, 5)
    test_candy.calculate_cost(4.5,2)
    assert candy < test_candy
    cookie = Cookie()
    test_cookie = Cookie()
    cookie.calculate_cost(4.99, 6)
    test_cookie.calculate_cost(4.99, 12)
    assert cookie < test_cookie
    