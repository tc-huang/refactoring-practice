from feature_envy.order import Order

class Customer:
    def __init__(self, name: str, order_amount: float):
        self.name = name
        self.order = Order(order_amount)
    
    def calculate_discount(self) -> float:
        # Feature envy: Customer class is accessing too much of Order's details
        if self.order.amount > 500:
            return self.order.amount * 0.1
        else:
            return 0
