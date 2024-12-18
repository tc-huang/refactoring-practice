from data_clump_primitive_obsession.booking import Booking

def test_calculate_total_price():
    booking = Booking("John Doe", "2024-12-25", "2024-12-30", 100)
    assert booking.calculate_total_price() == 500  # 5 nights * 100 per night = 500