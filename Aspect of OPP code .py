# Encapsulation: Wrapping data and methods that operate on the data into a single unit (class).

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__engine_status = "Off"  # Private variable to encapsulate the engine status

    def start_engine(self):
        self.__engine_status = "On"
        print("Engine started.")

    def stop_engine(self):
        self.__engine_status = "Off"
        print("Engine stopped.")

    def get_engine_status(self):
        return self.__engine_status


# Inheritance: Creating a new class by using an existing class.

class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity

    def charge_battery(self):
        print(f"Charging battery of {self.make} {self.model}.")

    # Abstraction: Hiding the details and showing only the necessary features of an object.

    def display_info(self):
        print(f"{self.make} {self.model} - Battery Capacity: {self.battery_capacity}")


# Polymorphism (Overriding): Providing a specific implementation .

class HybridCar(Car):
    def __init__(self, make, model, battery_capacity, fuel_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
        self.fuel_capacity = fuel_capacity

    # Overriding the display_info method to provide specific information for HybridCar
    def display_info(self):
        print(f"{self.make} {self.model} - Battery Capacity: {self.battery_capacity}, Fuel Capacity: {self.fuel_capacity}")


# Creating a new car
Super_car = Car("Porsche", "GT3S")
print(Super_car)
print("Car Engine Status:", Super_car.get_engine_status())
Super_car.start_engine()
print("Car Engine Status:", Super_car.get_engine_status())
Super_car.stop_engine()
print()

# Electric car
electric_car = ElectricCar("Tesla", "CyberTruck", "1000 kWh")
electric_car.display_info()
electric_car.start_engine()  # Electric cars don't have traditional engines, so the method will have a different behavior
electric_car.charge_battery()
electric_car.stop_engine()
print()

# Hybrid car
hybrid_car = HybridCar("Toyota", "Camry", "100 kWh", "40 liters")
hybrid_car.display_info()
hybrid_car.start_engine()
hybrid_car.stop_engine()


