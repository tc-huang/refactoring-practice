from srp.payment_method import PaymentMethod

class CreditCardPayment(PaymentMethod):

    def process_payment(self, amount: float) -> str:
        return f"Processed credit card payment of {amount}"