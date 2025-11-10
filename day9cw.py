class Vehicle:
    def __init__(self, vehicle_id, base_rate):
        self._vehicle_id = vehicle_id
        self._base_rate = base_rate

    def display_details(self):
        return f"Vehicle ID: {self._vehicle_id}, Base Rate: {self._base_rate}"

    def rental_charge(self):
        
        return 0.0

class Car(Vehicle):
    def __init__(self, vehicle_id, base_rate, num_seats):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats

    def rental_charge(self):
        return self._base_rate * self.num_seats

class Bike(Vehicle):
    def __init__(self, vehicle_id, base_rate, bike_type):
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type

    def rental_charge(self):
        return self._base_rate * 0.5

def calculate_rental(vehicle_obj):
    return vehicle_obj.rental_charge()

if __name__ == "__main__":
    car1 = Car("CAR001", 100.00, 4)
    bike1 = Bike("BIKE001", 80.00, "Scooter")

    print(car1.display_details())           # Vehicle ID: CAR001, Base Rate: 100.0
    print(f"Rental Charge: {calculate_rental(car1)}")  # Rental Charge: 400.0

    print(bike1.display_details())          # Vehicle ID: BIKE001, Base Rate: 80.0
    print(f"Rental Charge: {calculate_rental(bike1)}") # Rental Charge: 40.0
