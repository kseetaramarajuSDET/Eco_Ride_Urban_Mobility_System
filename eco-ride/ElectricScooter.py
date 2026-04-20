from Vehicle import Vehicle


class ElectricScooter(Vehicle):
    def __init__(self, vehicle_id, model, max_speed_limit):
        super().__init__(vehicle_id, model)
        self.max_speed_limit = max_speed_limit

    def __str__(self):
        print(super().__str__())
        return f'{self.max_speed_limit} km/hr speed limit'
