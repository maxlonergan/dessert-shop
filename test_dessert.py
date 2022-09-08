# content of test_sample.py

from dessert import *


def test_default():
    '''
    tests default values
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
    tests alternate values of each method
    '''
    candy = Candy(2.5,5.0,'peppermint')
    assert candy.candy_weight == 2.5
    assert candy.price_per_pound == 5.0
    assert candy.name == 'peppermint'

    cookie = Cookie(12,6.5,'chocolate chip')
    assert cookie.cookie_quantity == 12
    assert cookie.price_per_dozen == 6.5
    assert cookie.name == 'chocolate chip'

    ice_cream = IceCream(6,2.5,'vanilla')
    assert ice_cream.scoop_count == 6
    assert ice_cream.price_per_scoop == 2.5
    assert ice_cream.name == 'vanilla'

    sundae = Sundae('chocolate',4.0,'toppings')
    assert sundae.topping_name == 'chocolate'
    assert sundae.topping_price == 4.0
    assert sundae.name == 'toppings'
