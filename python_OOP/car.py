class Car:
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = 0.15
        else:
            self.tax = 0.12
        
    def display_all(self):
        output = "Price: " + str(self.price) + "\nSpeed: " + self.speed + "\nFuel: " + self.fuel + "\nMileage: " + self.mileage + "\nTax: " + str(self.tax)
        return output
        
car1 = Car(2000, "35mph", "Full", "15 mi")

print(car1.display_all())
