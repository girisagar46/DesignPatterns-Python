"""
In the case of module imports, we may accidently create an object even when it’s not needed.
Lazy instantiation makes sure that the object gets created when it’s actually needed.
"""

class LazySingleton(object):
	__instance = None
	def __init__(self):
		if not LazySingleton.__instance:
			print("__init__ method called...")
		else:
			print("Instance already created:", self.getInstance())

	@classmethod
	def getInstance(cls):
		print("getInstance() method called...")
		if not cls.__instance:
			cls.__instance = LazySingleton()
		return cls.__instance

s = LazySingleton() # class initialized but object not created
print("Object Created (s) ", LazySingleton().getInstance()) # object gets created here
s1 = LazySingleton() # Instance already created


# OUTPUT:
# __init__ method called...
# __init__ method called...
# getInstance() method called...
# __init__ method called...
# Object Created (s)  <__main__.LazySingleton object at 0x7f72d2c61ba8>
# getInstance() method called...
# Instance already created: <__main__.LazySingleton object at 0x7f72d2c61ba8>
