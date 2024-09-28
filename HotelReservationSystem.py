from datetime import datetime
from Customer import Customer
from Room import Room
from Reservation import Reservation
from Payment import Payment

class HotelReservationSystem:
    def __init__(self):
        # Sample data
        self.customers = []
        self.rooms = []
        self.reservations = []

    def add_customer(self, name, email, phone):
        customer = Customer(name, email, phone)
        self.customers.append(customer)
        return customer

    def add_room(self, room_number, room_type, price_per_night):
        room = Room(room_number, room_type, price_per_night)
        self.rooms.append(room)
        return room

    def make_reservation(self, customer, room, check_in, check_out):
        if room.book_room():
            reservation = Reservation(customer, room, check_in, check_out)
            self.reservations.append(reservation)
            payment = Payment(reservation, "Credit Card")
            payment.process_payment()
            print(reservation.get_reservation_details())
        else:
            print("Room is not available!")

# Testing the implementation
if __name__ == "__main__":
    system = HotelReservationSystem()

    # Adding a customer
    customer1 = system.add_customer("Ted Vera", "tedvera@mac.com", "555-1234")
    
    # Adding a room
    room1 = system.add_room(101, "Double", 89.95)

    # Making a reservation
    check_in_date = datetime(2023, 8, 22)
    check_out_date = datetime(2023, 8, 24)
    system.make_reservation(customer1, room1, check_in_date, check_out_date)
