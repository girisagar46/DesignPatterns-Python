class Dog:

    def __init__(self, name):
        """
        Initializer of Dog class
        :param name:
        """
        self._name = name

    def speak(self) -> str:
        return "Woof!"


class Cat:

    def __init__(self, name):
        """
        Initializer of Dog class
        :param name:
        """
        self._name = name

    def speak(self) -> str:
        return "Meow!"


def get_pet(pet: str="dog"):

    """
    This is the factory method.
    If new class is added, just add it's (key:val) pair in pets dictionary
    :returns: object
    :param: instance you want to get
    """

    pets = dict(dog=Dog('Nymeria'), cat=Cat("Tom"))

    return pets.get(pet)


if __name__ == '__main__':
    d = get_pet('dog')
    print(d.speak())

    c = get_pet('cat')
    print(c.speak())
