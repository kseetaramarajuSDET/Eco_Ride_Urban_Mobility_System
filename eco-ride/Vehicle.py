class Vehicle:

    def __init__(self, vehicle_id, model, battery):
        self.vehicle_id = vehicle_id
        self.model = model
        self.battery = battery

    def __str__(self):
        return f"Vehicle ID : {self.vehicle_id} Model : {self.model} Battery : {self.battery}"

