# ================================
# Assignment 1: Smartphone Class
# ================================

# Base class
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage  # in GB
        self.battery = battery  # in %

    # Method to display phone info
    def phone_info(self):
        print(f"📱 {self.brand} {self.model} - {self.storage}GB - Battery: {self.battery}%")

    # Method to charge the phone
    def charge(self, amount):
        self.battery += amount
        if self.battery > 100:
            self.battery = 100
        print(f"🔋 Charging... Battery at {self.battery}%")

# Derived class (Inheritance)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, cooling_system):
        super().__init__(brand, model, storage, battery)  # call parent constructor
        self.cooling_system = cooling_system  # new attribute

    # New method specific to gaming phones
    def play_game(self, game):
        if self.battery > 10:
            print(f"🎮 Playing {game} on {self.model} with {self.cooling_system} cooling.")
            self.battery -= 10
        else:
            print("⚠️ Battery too low to play games!")


# Example usage
phone1 = Smartphone("Samsung", "Galaxy S22", 128, 80)
phone2 = GamingPhone("Asus", "ROG Phone 7", 256, 50, "Liquid Cooling")

phone1.phone_info()
phone1.charge(15)

phone2.phone_info()
phone2.play_game("PUBG Mobile")
phone2.charge(30)
