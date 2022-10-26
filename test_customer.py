from dessertshop import Customer

def test_customer():
    '''
    tests attributes of the customer class
    '''
    customer = Customer('Steve')
    assert customer.customer_name == 'Steve'
    assert customer.customer_id == 1
    assert not customer.order_history
