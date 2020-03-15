#learning OOP to build the car

class Car():
    def __init__(self, make = 'none', model = 'none',price = 0, quantity = 0): # constructor of car classs
        self.make = make
        self.model = model
        self.price = price
        self.quantity = quantity
    # make the method of car where user will be asked which are is it
    def car_cost(self):
        print('%s %s @ %d= $%d' %(self.make, self.model,self.price, self.price * self.quantity))
        self.total = self.price * self.quantity
        return self.total

car = Car('honda', 'accord', 100,2)
print(car.car_cost())
        

