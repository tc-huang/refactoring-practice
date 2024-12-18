from feature_envy.customer import Customer

def test_calculate_discount():
    customer = Customer("John Doe", 1000)
    assert customer.calculate_discount() == 100  # Expected 10% discount for this example
