class Booking:
    def __init__(self, guest_name: str, start_date: str, end_date: str, price_per_night: float):
        self.guest_name = guest_name
        self.start_date = start_date
        self.end_date = end_date
        self.price_per_night = price_per_night
    
    def calculate_total_price(self) -> float:
        days = (int(self.end_date.split('-')[2]) - int(self.start_date.split('-')[2]))
        return days * self.price_per_night