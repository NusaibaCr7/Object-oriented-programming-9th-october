
class Vehicle:
    def __init__(self, max_speed, mileage, color):
        self.max_speed = max_speed
        self.mileage = mileage
        self.color = color
        
tesla = Vehicle(180,0, "White")
lambo = Vehicle(350, 3 , "Blue")

print("Tesla Max Speed:", tesla.max_speed)
print("Tesla Mileage:", tesla.mileage)
print("Tesla Color:", tesla.color)

print()

print("Lambo Max Speed:", lambo.max_speed)
print("Lambo Mileage:", lambo.mileage)
print("Lambo Color:", lambo.color)
