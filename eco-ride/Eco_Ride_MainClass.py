from importlib.util import source_hash
from time import process_time

from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter

from Vehicle import Vehicle

# vehicle = Vehicle("V101", "Honda")
# vehicle.maintenance_status = 'good'
# vehicle.battery = 90
# vehicle.rental_price = 2000
# print(vehicle)

vehicle = ElectricCar("V102", "HondaI20", 10)
vehicle.battery = 80
vehicle.rental_price = 3000
vehicle.maintenance_status = 'inservice'

print(vehicle)

vehicle1 = ElectricScooter("V103", "HondaShine", 50)
vehicle1.battery = 80
vehicle1.rental_price = 1000
vehicle1.maintenance_status = 'needrepair'

print(vehicle1)

print(vehicle.calculate_trip_cost(20))
print(vehicle1.calculate_trip_cost(10))

print("---------------")

# Create a mixed list (The "List of Objects")
fleet_to_process = [vehicle, vehicle1]

# Polymorphism in action
print("--- Processing Trip Receipts ---")
for v in fleet_to_process:
    # Here, 'units' is used as km for cars and minutes for scooters
    # Python decides which formula to use at RUNTIME.
    cost = v.calculate_trip_cost(20)
    print(f"Vehicle {v.vehicle_id} , Vehicle Model : {v.model} , Total Cost = ${cost}")
