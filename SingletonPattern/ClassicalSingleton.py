class classicalSingleton(object):
	"""
	We override	the	 __new__ method	(Python's special method to 
	instantiate objects) to control the object creation.
 	"""

 	def __new__(cls):
		# Check whether the object of that class exixts or not
		if not hasattr(cls, "instance"):
			cls.instance = super(classicalSingleton, cls).__new__(cls)
		return cls.instance

s = classicalSingleton()
print("Object Created: ", s)


s1 = classicalSingleton()
"""
Here s1  object is requested,  hasattr()  detects that an object already
exists and hence  s1  allocates the existing object instance at 0x7fe45e7ce350
"""
print("Object Created: ", s1)

# OUTPUT
# ('Object Created: ', <__main__.Singleton object at 0x7fe45e7ce350>)
# ('Object Created: ', <__main__.Singleton object at 0x7fe45e7ce350>)
