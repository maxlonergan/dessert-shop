'''
test cases for dessert.py
'''

from dessert import *

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
    assert sundae.name == ''

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

    sundae = Sundae('test sundae',1.50,'chocolate',4.0)
    assert sundae.name == 'test sundae'
    assert sundae.price_per_scoop == 1.50
    assert sundae.topping_name == 'chocolate'
    assert sundae.topping_price == 4.0

# tests conducted under this comment block should be following this guide
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
    sundae.topping_name = 'test name'
    assert sundae.topping_name == 'test name'
    sundae.topping_price = 4.0
    assert sundae.topping_price == 4.0

    sundae = Sundae('peanuts', 1.5, 'test name', 4.75)
    sundae.name = 'chocolate'
    assert sundae.name == 'chocolate'
    sundae.price_per_scoop = 2.75
    assert sundae.price_per_scoop == 2.75
    sundae.topping_name = 'candy'
    assert sundae.topping_name == 'candy'
    sundae.topping_price = 6.75
    assert sundae.topping_price == 6.75
