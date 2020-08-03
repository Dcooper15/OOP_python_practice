class Vehicle:


    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __str__(self):
        return "My car is a %d %s %s." % (self.year, self.make, self.model)



my_car = Vehicle("Jeep", "Patriot", 2014)

print(my_car)
    



    