from abc import ABCMeta, abstractmethod

# Abstract Factory
class PizzaFactory(metaclass = ABCMeta):

	@abstractmethod
	def createVegPizza(self):
		pass


	@abstractmethod
	def createNonVegPizza(self):
		pass


# Concrete Factories
class NepalPizzaFactory(PizzaFactory):
	def createVegPizza(self):
		return DeluxeVegPizza()

	def createNonVegPizza(self):
		return ChickenPizza()

class USPizzaFactory(PizzaFactory):
	def createVegPizza(self):
		return MexicanPizza()

	def createNonVegPizza(self):
		return HamPizza()

# Abstract Product
class VegPizza(metaclass = ABCMeta):
	@abstractmethod
	def prepare(self):
		pass

class NonVegPizza(metaclass = ABCMeta):
	@abstractmethod
	def serve(self, NonVegPizza):
		pass

# Concrete Product
class DeluxeVegPizza(VegPizza):
	def prepare(self):
		print("Prepare ", type(self).__name__)

class ChickenPizza(NonVegPizza):
	def serve(self, VegPizza):
		print(type(self).__name__, " is served with Chicken on ", type(VegPizza).__name__)

class MexicanPizza(VegPizza):
	def prepare(self):
		print("Prepare ", type(self).__name__)

class HamPizza(NonVegPizza):
	def serve(self, VegPizza):
		print(type(self).__name__, " is served with Ham on ", type(VegPizza).__name__)

class PizzaStore(object):
	def __init__(self):
		pass

	def makePizzas(self):
		for factory in [NepalPizzaFactory(), USPizzaFactory()]:
			self.factory = factory
			self.NonVegPizza = self.factory.createNonVegPizza()
			self.VegPizza = self.factory.createVegPizza()
			self.VegPizza.prepare()
			self.NonVegPizza.serve(self.VegPizza)


pizza = PizzaStore()
pizza.makePizzas()