class Reservation:
    def __init__(self, customer, room, check_in_date, check_out_date):
        self.customer = customer        # Instance of Customer
        self.room = room                # Instance of Room
        self.check_in_date = check_in_date  # Check-in date
        self.check_out_date = check_out_date  # Check-out date
        self.total_cost = self.calculate_cost()  # Calculate total cost upon reservation

    def calculate_cost(self):
        nights = (self.check_out_date - self.check_in_date).days  # Calculate number of nights
        return nights * self.room.price_per_night  # Total cost

    def get_reservation_details(self):
        return (f"Reservation Details:\n"
                f"Customer: {self.customer.get_details()}\n"
                f"Room: {self.room.get_room_details()}\n"
                f"Check-in: {self.check_in_date}\n"
                f"Check-out: {self.check_out_date}\n"
                f"Total Cost: {self.total_cost}")
