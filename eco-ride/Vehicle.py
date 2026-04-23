from abc import ABC, abstractmethod


class Vehicle(ABC):

    def __init__(self, vehicle_id, model):
        self.vehicle_id = vehicle_id
        self.model = model
        # private members
        self.__battery = 0
        self.__maintenance_status = 'empty'
        self.__rental_price = 0.0

    # ALL Abstract Methods
    @abstractmethod
    def calculate_trip_cost(self, distance):
        pass

    # --- GETTER & SETTER for maintenance_status ---
    @property
    def maintenance_status(self):
        return self.__maintenance_status

    @maintenance_status.setter
    def maintenance_status(self, value):
        valid_status = ['Available', 'OnTrip', 'UnderMaintenance', 'Broken']
        if value in valid_status:
            self.__maintenance_status = value
        else:
            print('Invalid maintenance status')

    # --- GETTER & SETTER for battery ---
    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        if 0 <= value <= 100:
            self.__battery = value
        else:
            print(f"Error: Invalid battery value {value}. Must be between 0-100.")

    # --- GETTER & SETTER for Rental Price ---
    @property
    def rental_price(self):
        return self.__rental_price

    @rental_price.setter
    def rental_price(self, value):
        if value > 0:
            self.__rental_price = value
        else:
            print(f"Error: Invalid rental price value {value}. Must be positive.")

    def __str__(self):
        return f" Vehicle ID : {self.vehicle_id} Model : {self.model} Battery : {self.battery} Maintenance_status : {self.maintenance_status} Rental price : {self.rental_price}"

    def __eq__(self, other):
        # 1. Safety check: is the other thing a Vehicle?
        if not isinstance(other, Vehicle):
            return False
        # 2. Comparison: Do they have the same ID?
        return self.vehicle_id == other.vehicle_id
