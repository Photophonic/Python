class Dog:
    """a simple class for dogs"""

    # a funtion that is part of a class is a method
    # Python will use two leading and trailing __ to denote this method
    # self must come first as this will be used for later instance creation
    def __init__(self, name, age):
        """initialize self variables"""
        # these are attributes of the class
        self.name = name
        self.age = age
    # additional methods in the class

    def sit(self):
        """simulates dog sitting"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simulates dog rolling over"""
        print(f"{self.name} is rolling over")


my_dog = Dog('Sebastian', 9)
print(f"My dog's name is {my_dog.name} and he is {my_dog.age}")
my_dog.roll_over()
my_dog.sit()

your_dog = Dog('Ein', 6)
print(f"Your dog's name is {your_dog.name} and they are {your_dog.age}")
my_dog.sit()
your_dog.sit()
