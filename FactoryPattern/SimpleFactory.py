from abc import ABCMeta, abstractmethod

class Animal(metaclass = ABCMeta):
	# ABCMeta is Python’s special metaclass to make a class Abstract
	@abstractmethod
	def do_say(self):
		pass

class Dog(Animal):
	def do_say(self):
		print("Bhow Bhow!!")


class Cat(Animal):
	def do_say(self):
		print("Meow Meow!!")

class ForestFactory(object): 
	# takes user input and evaluates do_say() method
	def make_sound(self, object_type):
		return eval(object_type)().do_say()

if __name__ == '__main__':
	ff = ForestFactory()
	animal = input("Which Animal ?")
	ff.make_sound(animal)