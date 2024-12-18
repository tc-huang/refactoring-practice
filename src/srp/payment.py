class PaymentProcessor:
    
    def process_payment(self, payment_method: str, amount: float) -> str:
        if payment_method == "credit_card":
            return f"Processed credit card payment of {amount}"
        elif payment_method == "paypal":
            return f"Processed PayPal payment of {amount}"
        elif payment_method == "apple_pay":
            return f"Processed Apple Pay payment of {amount}"
        else:
            raise ValueError("Unsupported payment method")
