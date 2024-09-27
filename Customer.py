class Customer:
    def __init__(self, name, email, phone):
        self.name = name              # Customer's name
        self.email = email            # Customer's email
        self.phone = phone            # Customer's phone number

    def get_details(self):
        return f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}"

    def update_email(self, new_email):
        self.email = new_email        # Update the customer's email

    def update_phone(self, new_phone):
        self.phone = new_phone        # Update the customer's phone number
