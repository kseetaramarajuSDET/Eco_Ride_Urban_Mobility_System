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

    def get_categorized_view(self, vehicle_list):
        # UC 9: Mapping Dictionary
        category_map = {
            "ElectricCar": [],
            "ElectricScooter": []
        }

        # Sorting the vehicles into the map
        for v in vehicle_list:
            if isinstance(v, ElectricCar):
                category_map["ElectricCar"].append(v)
            elif isinstance(v, ElectricScooter):
                category_map["ElectricScooter"].append(v)

        # Displaying the Categorized View
        for v_type, v_list in category_map.items():
            print(f"\n=== {v_type.upper()} SECTION ===")
            if not v_list:
                print("No vehicles in this category.")
            else:
                for v in v_list:
                    print(v)

    def get_fleet_analytics(self, all_vehicles):
        # UC 10: Initialize the counter dictionary
        stats = {}

        # Iterate and Tally
        for v in all_vehicles:
            # Assuming maintenance_status is the attribute from UC 2
            status = v.maintenance_status

            if status in stats:
                stats[status] += 1
            else:
                # Handle unexpected status values
                stats[status] = 1

        # Display Result in Formatted Summary
        print("\n" + "=" * 30)
        print("   FLEET ANALYTICS SUMMARY")
        print("=" * 30)
        for status, count in stats.items():
            print(f" {status:<18}: {count}")
        print("=" * 30)
        print(f" TOTAL FLEET SIZE  : {len(all_vehicles)}")

    def sort_by_model(self, hub_name):
        if hub_name not in self.__hubs:
            print("Hub not found.")
            return

        original_list = self.__hubs[hub_name]

        # UC 11: Sort by Model name using a Lambda key
        # It compares 'Tesla' vs 'Audi' vs 'BMW'
        sorted_list = sorted(original_list, key=lambda v: v.model)

        print(f"\n--- Alphabetical Fleet in {hub_name} ---")
        for vehicle in sorted_list:
            # This automatically calls the __str__ method we wrote above!
            print(vehicle)

    def sort_by_battery_percentage(self, hub_name):
        if hub_name not in self.__hubs:
            print("Hub not found.")
            return

        original_list = self.__hubs[hub_name]

        sorted_list = sorted(original_list, key=lambda v: v.battery, reverse=True)
        print(f"\n--- Sorted Vehicles Based On Battery Percentage in {hub_name} ---")
        for vehicle in sorted_list:
            # This automatically calls the __str__ method we wrote above!
            print(vehicle)

    def sort_by_farePrice(self, hub_name, distance, mins):
        if hub_name not in self.__hubs:
            print("Hub not found.")
            return

        original_list = self.__hubs[hub_name]

        def calculate_fareprice_for_all_type_of_vehicles(vehicle):
            if isinstance(vehicle, ElectricCar):
                return vehicle.calculate_trip_cost(distance)
            elif isinstance(vehicle, ElectricScooter):
                return vehicle.calculate_trip_cost(mins)
            else:
                print(f"Vehicle {vehicle.vehicle_id} not found.")
                return 0

        sorted_list = sorted(original_list, key=calculate_fareprice_for_all_type_of_vehicles)

        print(f"\n--- Sorted Vehicles Based On Fare Price in {hub_name} ---")
        for vehicle in sorted_list:
            # This automatically calls the __str__ method we wrote above!
            print(f"{vehicle} | Fare: ${calculate_fareprice_for_all_type_of_vehicles(vehicle):.2f}")
