"""
the concept is based on all objects sharing the same state, hence, known as the Monostate pattern.
Also known as Borg pattern
"""

class Borg(object):
	__shared_state = {"1":"2"}
	def __init__(self):
		self.y = 1
		print("before----->",self.__dict__)
		self.__dict__ = self.__shared_state
		print("after----->",self.__dict__)
		pass

b = Borg()
b1 = Borg()
b.y = 4

print("Borg object 'b': ", b)
print("Borg object 'b1': ", b1)

## b and b1 shares same shared variable
print("Object State 'b': ", b.__dict__)
print("Object State 'b1': ", b1.__dict__)

class BorgTweaked(object):
	__shared_state = {}
	def __new__(cls, *args, **kwargs):
		obj = super(BorgTweaked, cls).__new__(cls, *args, **kwargs)
		obj.__dict__ = cls.__shared_state
		return obj

bt = BorgTweaked()
bt2 = BorgTweaked()
bt.x = 1
print(bt.__dict__)
print(bt2.__dict__)