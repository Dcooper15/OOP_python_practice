class Mammal:
    def __init__(self, name, type_of_mammal, breed, legs):
        self.name = name
        self.type_of_mammal = type_of_mammal
        self.breed = breed
        self.legs = legs

    def eat(self):
        return "%s is eating" % (self.type_of_mammal)

class Cat(Mammal):
    def __init__(self, name, type_of_mammal, breed, legs, fur):
        super().__init__(name, type_of_mammal, breed, legs)
        self.fur = fur

    def __str__(self):
        return "%s is a %s %s breed with %d legs and %s fur." % (self.name, self.type_of_mammal, self.breed, self.legs, self.fur)

    def eat(self):
        return "This is returned because it is a subclass of mammal!!"



finnbar = Cat("Finnbar", "cat", "mixed", 4, "short hair")
onyx = Cat("Onyx", "cat", "bombay", 4, "short hair" )
print(finnbar, onyx)
print(finnbar.eat())