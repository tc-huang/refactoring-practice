from data_clump_primitive_obsession.date_range import DateRange

class Booking:
    def __init__(self, guest_name: str, date_range: DateRange, price_per_night: float):
        self.guest_name = guest_name
        self.date_range = date_range
        self.price_per_night = price_per_night
    
    def calculate_total_price(self) -> float:
        days = self.date_range.get_number_of_days()
        return days * self.price_per_night