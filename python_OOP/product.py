class Product:
    def __init__(self, name, price, weight, brand):
        self.name = name
        self.price = price
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "sold"
        return self
    
    def add_tax(self, tax):
        self.price += self.price * tax
        return self
    
    def return_item(self, reason_for_return):
        if reason_for_return == "defective":
            self.status = "defective"
            self.price = 0
        elif reason_for_return == "like_new":
            self.status = "for sale"
        elif reason_for_return == "opened":
            self.status = "used"
            self.add_tax(-0.2)
        return self
    
    def display_info(self):
        print("Name: ", self.name, "\nPrice: $", self.price, "\nWeight: ", self.weight, "\nBrand: ", self.brand, "\nStatus: ", self.status)
        return self

jordan1 = Product("Jordan 1", 180, 1.4, "Jordan")

jordan1.display_info()
jordan1.return_item("opened").display_info()