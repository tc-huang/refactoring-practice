from srp.craditcard_payment import CreditCardPayment
from srp.paypal_payment import PayPalPayment
from srp.applepay_payment import ApplePayPayment

class PaymentProcessor:

    def __init__(self):
        self.payment_methods = {
            "credit_card": CreditCardPayment(),
            "paypal": PayPalPayment(),
            "apple_pay": ApplePayPayment(),
        }

    def process_payment(self, payment_method: str, amount: float) -> str:
        if payment_method not in self.payment_methods:
            raise ValueError("Unsupported payment method")
        payment_strategy = self.payment_methods[payment_method]
        return payment_strategy.process_payment(amount)
