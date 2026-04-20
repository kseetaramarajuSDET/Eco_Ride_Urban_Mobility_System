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

vehicle = ElectricScooter("V103", "HondaShine", 50)
vehicle.battery = 80
vehicle.rental_price = 1000
vehicle.maintenance_status = 'needrepair'

print(vehicle)
