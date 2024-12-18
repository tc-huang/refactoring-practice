from srp.payment_method import PaymentMethod

class ApplePayPayment(PaymentMethod):

    def process_payment(self, amount: float) -> str:
        return f"Processed Apple Pay payment of {amount}"