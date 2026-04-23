from Vehicle import Vehicle
from ElectricCar import *
from ElectricScooter import *


class FleetHubManager:

    def __init__(self):
        self.__hubs = {}

    def add_hub(self, hub):
        hub = hub.strip()
        if hub not in self.__hubs:
            self.__hubs[hub] = []
            print(f"Hub '{hub}' established.")
        else:
            print(f"hub : {hub} already Exists !!")

    def display_all_hubs(self):
        if not self.__hubs:
            print("No Hubs registered !")
            return
        for hub, vehicles in self.__hubs.items():
            print(f" Hub : {hub} Vehicles : {len(vehicles)}")
            if not vehicles:
                print("No vehicles registered !")
            for v in vehicles:
                # Polymorphism in action: calling __str__ or specific methods
                print(v)

    def add_vehicle(self, hub, vehicle):
        if hub not in self.__hubs:
            print(f"Hub '{hub}' not registered !")
            return

        if vehicle in self.__hubs[hub]:
            print(f"ALARM: Duplicate ID '{vehicle.vehicle_id}' detected! Entry blocked.")
        else:
            self.__hubs[hub].append(vehicle)
            print(f"Vehicle {vehicle.vehicle_id} successfully parked in {hub}.")

    def search_vehicle_by_battery_percentage(self, hub, battery_percentage):
        if hub not in self.__hubs:
            print(f"Hub '{hub}' not registered !")
            return

        vehicle_list = self.__hubs[hub]

        result_list = list(filter(lambda v: v.battery > battery_percentage, vehicle_list))

        # Display results
        print(f"\n--- High Battery Vehicles in {hub} ---")

        if not result_list:
            print("No vehicles found with battery percentage More Than " + str(battery_percentage))
        for vehicle in result_list:
            print(" Vehicles Which Having More Battery Percentage Than " + str(battery_percentage))
            print(vehicle)

# hub_name = input("Enter Hub Name to add vehicle to: ").strip()
# if hub_name not in self.__hubs:
#     print("Error: Hub not found. Please create it first.")
#     return
# v_id = input("Enter Vehicle ID to move to this hub:").strip()
# # Search for the vehicle in your global inventory
# target_vehicle = next((v for v in vehicle_list if v.vehicle_id == v_id), None)
# if target_vehicle:
#     self.__hubs[hub_name].append(target_vehicle)
#     print(f"Vehicle '{target_vehicle}' added to hub '{hub_name}' !")
# else:
#     print("Error: Vehicle ID not found in system inventory.")
