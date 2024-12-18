from srp.payment import PaymentProcessor

def test_process_payment_credit_card():
    processor = PaymentProcessor()
    result = processor.process_payment("credit_card", 100)
    assert result == "Processed credit card payment of 100"

def test_process_payment_paypal():
    processor = PaymentProcessor()
    result = processor.process_payment("paypal", 200)
    assert result == "Processed PayPal payment of 200"

def test_process_payment_apple_pay():
    processor = PaymentProcessor()
    result = processor.process_payment("apple_pay", 300)
    assert result == "Processed Apple Pay payment of 300"