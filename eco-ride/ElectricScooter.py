from Vehicle import Vehicle


class ElectricScooter(Vehicle):
    def calculate_trip_cost(self, minutes):
        # Formula: $1.00 base + $0.15 per minute
        return 1.00 + (0.15 * minutes)

    def __init__(self, vehicle_id, model, max_speed_limit):
        super().__init__(vehicle_id, model)
        self.max_speed_limit = max_speed_limit

    def __str__(self):
        print(super().__str__())
        return f'{self.max_speed_limit} km/hr speed limit'
