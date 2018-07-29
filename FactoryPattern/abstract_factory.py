"""
Yield multiple, related object. Which class to get is not known until runtime

(Solution) Abstract factory consists of
 - Abstract Factory
 - Concrete Factory
 - Abstract Product
 - Concrete Product
"""


class Dog:
    """One of the object to be returned"""

    def speak(self):
        return "Woof!"

    def __str__(self):
        return self.__class__.__name__


class DogFactory:
    """
    This is the concrete factory
    - Concrete factory generates concrete objects
    """

    def get_pet(self):
        """Returns Dog object"""
        return Dog()

    def get_food(self):
        """Returns Dog food"""
        return "Dog food"


class PetStore:

    def __init__(self, pet_factory=None):
        """ pet_factory is the abstract factory"""
        self._pet_factory = pet_factory

    def show_pet(self):
        """This is utility method"""
        pet = self._pet_factory.get_pet()
        pet_food = self._pet_factory.get_food()

        print(f"Pet {pet}")
        print(f"Pet says {pet.speak()}")
        print(f"Pet eats {pet_food}")

# create Concrete factory
factory = DogFactory()

shop = PetStore(factory)

shop.show_pet()