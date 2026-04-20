from Vehicle import Vehicle


class ElectricCar(Vehicle):

    def calculate_trip_cost(self,distance):
        # Formula: $5.00 base + $0.50 per km
        return 5.00 + (0.50 * distance)

    def __init__(self, vehicle_id, model, seating_capacity):
        super().__init__(vehicle_id, model)
        self.seating_capacity = seating_capacity

    def __str__(self):
        print(super().__str__())
        return f'{self.seating_capacity} seating car'
