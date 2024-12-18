class Order:
    def __init__(self, amount: float):
        self.amount = amount

    def get_discount_amount(self) -> float:
        if self.amount > 500:
            return self.amount * 0.1
        else:
            return 0
