class Bike:
    def __init__(self,price,max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0

    def displayInfo(self):
        print("Price:", self.price)
        print("Max Speed:", self.max_speed)
        print("Miles:", self.miles)
        return self

    def ride(self):
        print("Riding...")
        self.miles += 10
        return self
    
    def reverse(self):
        print("Reversing...")
        if self.miles >= 5:
            self.miles -= 5
        else:
            self.miles = 0
        return self
    
bike1 = Bike(200,"25mph")

bike1.ride().ride().ride().reverse().displayInfo()
