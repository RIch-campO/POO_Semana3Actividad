class Vehicle:
    """
    Base class representing a generic vehicle.
    Demonstrates ENCAPSULATION.
    """

    # In Python 3 we use 'Type Hints' (ej: brand: str) to indicate the data type
    def __init__(self, brand: str, model: str) -> None:
        # --- ENCAPSULATION ---
        # Private attributes denoted by double underscore (__).
        self.__brand = brand
        self.__model = model
        print(f"-> New Vehicle created: {self.__brand} {self.__model}")

    # 'Getter' methods
    def get_brand(self) -> str:
        return self.__brand

    def get_model(self) -> str:
        return self.__model


    # --- BASE METHOD ---
    def move(self) -> None:
        print("The vehicle performs a generic movement.")
