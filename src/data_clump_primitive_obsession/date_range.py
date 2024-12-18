class DateRange:
    def __init__(self, start_date: str, end_date: str):
        self.start_date = start_date
        self.end_date = end_date
    
    def get_number_of_days(self) -> int:
        start_day = int(self.start_date.split('-')[2])
        end_day = int(self.end_date.split('-')[2])
        return end_day - start_day