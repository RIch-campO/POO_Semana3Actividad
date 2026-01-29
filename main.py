
from Vehiculo import Vehicle
from Transportes import Airplane, Boat, Car
print("--- CREATING OBJECTS ---")

my_vehicle = Vehicle("Generic", "Model X")
my_plane = Airplane("Boeing", "747", 35000)
my_boat = Boat("Yamaha", "WaveRunner", False)
my_car = Car("Toyota", "Corolla", 4)

print("\n--- POLYMORPHISM IN ACTION ---")

fleet = [my_vehicle, my_plane, my_boat, my_car]

for v in fleet:
    v.move()
