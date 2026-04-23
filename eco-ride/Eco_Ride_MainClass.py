from importlib.util import source_hash
from time import process_time

from ElectricCar import ElectricCar
from ElectricScooter import ElectricScooter
from FleetHubManager import *

from Vehicle import Vehicle

# vehicle = Vehicle("V101", "Honda")
# vehicle.maintenance_status = 'good'
# vehicle.battery = 90
# vehicle.rental_price = 2000
# print(vehicle)

v1 = ElectricCar("V102", "HondaI20", 10)
v1.battery = 80
v1.rental_price = 3000
v1.maintenance_status = 'OnTrip'

# print(v1)

v2 = ElectricScooter("V103", "HondaShine", 50)
v2.battery = 60
v2.rental_price = 1000
v2.maintenance_status = 'UnderMaintenance'

# print(v2)

# print(v1.calculate_trip_cost(20))
# print(v2.calculate_trip_cost(10))

# print("---------------")

# Create a mixed list (The "List of Objects")
# fleet_to_process = [v1, v2]

# Polymorphism in action
# print("--- Processing Trip Receipts ---")
# for v in fleet_to_process:
#     # Here, 'units' is used as km for cars and minutes for scooters
#     # Python decides which formula to use at RUNTIME.
#     cost = v.calculate_trip_cost(20)
#     print(f"Vehicle {v.vehicle_id} , Vehicle Model : {v.model} , Total Cost = ${cost}")


#  UC6
v3 = ElectricCar("V105", "BMW", 6)
v3.battery = 90
v3.rental_price = 6000
v3.maintenance_status = 'Available'

# print(v3)
v4 = ElectricScooter("V104", "pulser220", 50)
v4.battery = 70
v4.rental_price = 2000
v4.maintenance_status = 'Broken'

# vehicle_list = [v1, v2, v3, v4, v1]

fleet = FleetHubManager()
# fleet.add_hub()
# fleet.add_vehicle(vehicle_list)
# print("-------------------")
# fleet.add_hub()
# fleet.add_vehicle(vehicle_list)
# print("-------------------")
# fleet.add_hub()
# fleet.add_vehicle(vehicle_list)
# print("-------------------")
# fleet.add_hub()
# fleet.add_vehicle(vehicle_list)
# print("-------------------")
# fleet.add_hub()
# fleet.add_vehicle(vehicle_list)


# UC7

fleet.add_hub("chennai")
fleet.add_hub("mumbai")
fleet.add_vehicle("chennai", v1)
fleet.add_vehicle("chennai", v2)
fleet.add_vehicle("mumbai", v3)
fleet.add_vehicle("mumbai", v4)
# fleet.add_vehicle("chennai", v1)
# fleet.display_all_hubs()


# UC8

# fleet.search_vehicle_by_battery_percentage("chennai", 70)
# print("---------------")
# fleet.search_vehicle_by_battery_percentage("mumbai", 70)

# UC9

vehicle_list = [v1, v2, v3, v4]

# fleet.get_categorized_view(vehicle_list)

# UC10

# fleet.get_fleet_analytics(vehicle_list)

# UC11
# fleet.display_sorted_hub("chennai")
# fleet.display_sorted_hub("mumbai")

# UC12

fleet.sort_by_battery_percentage("chennai")
fleet.sort_by_battery_percentage("mumbai")
print("=*30")

fleet.sort_by_farePrice("chennai", 40, 90)
fleet.sort_by_farePrice("mumbai", 40, 120)
