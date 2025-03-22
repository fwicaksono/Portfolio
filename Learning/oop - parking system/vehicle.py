from datetime import datetime

class Vehicle:
    def __init__(self, plate_number):
        self.plate_number = plate_number
        self.entry_time = None
        self.exit_time = None

    def enter_parking(self):
        self.entry_time = datetime.now()

    def exit_parking(self):
        self.exit_time = datetime.now()

    def calculate_parking_fee(self, rate_per_hour):
        if self.entry_time and self.exit_time:
            duration = (self.exit_time - self.entry_time).total_seconds() / 3600  # Konversi detik ke jam
            duration = max(1, round(duration))  # Minimal 1 jam
            return duration * rate_per_hour
        return 0

class Car(Vehicle):
    PARKING_RATE = 5000  # Tarif per jam untuk mobil

    def calculate_parking_fee(self):
        return super().calculate_parking_fee(Car.PARKING_RATE)

class Motorcycle(Vehicle):
    PARKING_RATE = 3000  # Tarif per jam untuk motor

    def calculate_parking_fee(self):
        return super().calculate_parking_fee(Motorcycle.PARKING_RATE)
