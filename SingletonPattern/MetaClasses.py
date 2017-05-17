"""
A metaclass is a class of a class, which means that the class is an instance of its metaclass. 
With metaclasses, programmers get an opportunity to create classes of their own type from the predefined Python classes.
"""

class MyInt(type):
	@classmethod
	def __call__(cls, *args, **kwargs):
		print("**** MY INT ****", args)
		print("Play with your objects")
		return type.__call__(cls, *args, **kwargs)

class int(metaclass = MyInt):
	def __init__(self, x, y):	
		self.x = x
		self.y = y

i = int(4,5)
