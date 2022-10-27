'''
you may need to comment out main() in dessertshop.py for pytest
to run properly
'''

from dessertshop import Customer
from dessertshop import check_database
from dessertshop import customer_db


def test_customer():
    '''
    tests attributes of the customer class
    '''
    customer = Customer('Steve')
    assert customer.customer_name == 'Steve'
    assert customer.customer_id == 1
    assert not customer.order_history

def test_id():
    '''
    tests to make sure each ID is unique
    '''
    test_order = []
    check_database(customer_db, 'steve',test_order)
    check_database(customer_db, 'nancy', test_order)
    check_database(customer_db, 'bob', test_order)
    assert customer_db['steve'].customer_id == 1002
    assert customer_db['nancy'].customer_id == 1003
    assert customer_db['bob'].customer_id == 1004
