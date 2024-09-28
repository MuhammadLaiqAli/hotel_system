class Room:
    def __init__(self, room_number, room_type, price_per_night):
        self.room_number = room_number  # Room number
        self.room_type = room_type      # Type of the room (e.g., single, double)
        self.price_per_night = price_per_night  # Price per night for the room
        self.is_available = True        # Room availability status

    def book_room(self):
        if self.is_available:
            self.is_available = False  # Mark the room as booked
            return True
        return False

    def release_room(self):
        self.is_available = True       # Mark the room as available again

    def get_room_details(self):
        return f"Room Number: {self.room_number}, Type: {self.room_type}, Price per Night: {self.price_per_night}, Available: {self.is_available}"
