# Python OOP Assignment: Classes & Polymorphism  

This project demonstrates **Object-Oriented Programming (OOP) concepts in Python**, including:  
- Class creation with attributes & methods  
- Constructors (`__init__`)  
- Inheritance  
- Encapsulation (via methods)  
- Polymorphism  

---

## 🏗️ Assignment 1: Design Your Own Class  

- **Class:** `Smartphone`  
- **Attributes:** brand, model, storage, battery  
- **Methods:**  
  - `phone_info()` → Displays phone details  
  - `charge(amount)` → Increases battery percentage  

- **Subclass:** `GamingPhone` (inherits from `Smartphone`)  
  - Extra attribute: `cooling_system`  
  - Extra method: `play_game(game)` → Simulates gaming and reduces battery  

**Example Run:**  
```python
phone1 = Smartphone("Samsung", "Galaxy S22", 128, 80)
phone1.phone_info()
phone1.charge(15)

phone2 = GamingPhone("Asus", "ROG Phone 7", 256, 50, "Liquid Cooling")
phone2.phone_info()
phone2.play_game("PUBG Mobile")
