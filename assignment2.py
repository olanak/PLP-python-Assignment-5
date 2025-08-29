# ================================
# Activity 2: Polymorphism Challenge
# ================================

class Animal:
    def move(self):
        print("This animal moves in some way...")

class Dog(Animal):
    def move(self):
        print("🐕 The dog runs on four legs.")

class Bird(Animal):
    def move(self):
        print("🐦 The bird flies in the sky.")

class Fish(Animal):
    def move(self):
        print("🐟 The fish swims in water.")

# Example usage
animals = [Dog(), Bird(), Fish()]

for animal in animals:
    animal.move()  # Each class has its own implementation
