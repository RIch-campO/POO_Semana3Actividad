# ==========================================
# PART 2: INHERITANCE & POLYMORPHISM
# ==========================================

from Vehiculo import Vehicle
class Airplane(Vehicle):
    """ Subclass for Airplanes (Avion). """

    def __init__(self, brand: str, model: str, max_altitude: float) -> None:
        super().__init__(brand, model)

        # Private attribute specific to Airplane
        self.__max_altitude = max_altitude

    # --- POLYMORPHISM (Override) ---
    def move(self) -> None:
        print(f"[Airplane] The {self.get_brand()} flies in the air at a max altitude of {self.__max_altitude} feet.")


class Boat(Vehicle):
    """ Subclass for Boats (Barco). """

    def __init__(self, brand: str, model: str, is_sailboat: bool) -> None:
        super().__init__(brand, model)

        # Private attribute specific to Boat
        self.__is_sailboat = is_sailboat

    # --- POLYMORPHISM (Override) ---
    def move(self) -> None:
        # Ternary operator in Python
        boat_type = "sailboat" if self.__is_sailboat else "motorboat"
        print(f"[Boat] The {boat_type} {self.get_brand()} sails on the water.")
class Car(Vehicle):
    def __init__(self, brand: str, model: str, num_doors: int) -> None:
        super().__init__(brand, model)

        #Private attribute specific to Car
        self.__num_doors = num_doors

# ==========================================
# PART 3: EXECUTION (OOP IN ACTION)
# ==========================================

# if __name__ == "__main__":
print("--- CREATING OBJECTS ---")
# Python 3 handles these instantiations cleanly
my_car = Vehicle(brand="Toyota", model="Corolla")
my_jet = Airplane(brand="Boeing", model="747", max_altitude=35000.0)
my_boat = Boat(brand="Yamaha", model="WaveRunner", is_sailboat=False)

print("\n--- DEMONSTRATING POLYMORPHISM ---")

# Using a list to demonstrate that Python treats them all as objects capable of 'move()'
transport_fleet = [my_car, my_jet, my_boat]

for vehicle in transport_fleet:
    vehicle.move()  # Python 3 resolves the correct method at runtime