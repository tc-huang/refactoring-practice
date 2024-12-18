from feature_envy.order import Order

class Customer:
    def __init__(self, name: str, order_amount: float):
        self.name = name
        self.order = Order(order_amount)
    
    def calculate_discount(self) -> float:
        return self.order.get_discount_amount()
