from srp.payment_method import PaymentMethod

class PayPalPayment(PaymentMethod):

    def process_payment(self, amount: float) -> str:
        return f"Processed PayPal payment of {amount}"