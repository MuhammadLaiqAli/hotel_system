class Payment:
    def __init__(self, reservation, payment_method):
        self.reservation = reservation  # Instance of Reservation
        self.payment_method = payment_method  # Payment method (e.g., credit card)

    def process_payment(self):
        # Placeholder for payment processing logic
        print(f"Processing payment of {self.reservation.total_cost} via {self.payment_method}")
        return True  # Assume payment is successful

    def get_payment_details(self):
        return (f"Payment Details:\n"
                f"Reservation Cost: {self.reservation.total_cost}\n"
                f"Payment Method: {self.payment_method}")
