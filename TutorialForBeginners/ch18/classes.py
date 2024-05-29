# classes are capitalized
# define a blueprint
class Vehicle:
    # create properties with an initializer
    def __init__(self, make, model):
        # references itself with the initial properties.
        # somewhate similar to THIS in Java
        self.make = make
        self.model = model

    # define methods the object can take in the class
    def moves(self):
        print("Moves along...")

    # define another method, using a getter
    def get_make_model(self):
        # reference itself to get the make and model
        print(f"I'm a {self.make} - {self.model}.")


# create an object from the class and pass in init values
my_car = Vehicle("Toyota", "4Runner")
kelly_car = Vehicle("Mini", "Countryman")

# print the make.model values
# print(my_car.make, my_car.model)
my_car.get_make_model()
# call the method on our new object
my_car.moves()

kelly_car.get_make_model()
kelly_car.moves()


# Inheritance allows us to define a class that inherits all the methods and properties from another class.
class Airplane(Vehicle):
    # this will overwrite what it receives from the parent Vehicle class

    # add your own properties to the inherited class
    def __init__(self, make, model, faa_id):
        # use super().__init__ to redefine the initializer
        super().__init__(make, model)
        self.faa_id = faa_id

    def get_faa_id(self):
        print(self.faa_id)

    def moves(self):
        print("Flies along..")


class Truck(Vehicle):
    def moves(self):
        print("Trundles along..")


class GolfCart(Vehicle):
    # this will allow you to inherit everything from parent
    pass


# still requires a make/model
my_plane = Airplane("Plane", "Blue", "F12345")

my_plane.get_make_model()
my_plane.moves()
my_plane.get_faa_id()


# polymorphism
# the output will change despite havinging the same methods
for v in (my_car, kelly_car, my_plane):
    v.get_make_model()
    v.moves()
