class MetaSingleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			print("here", cls._instances)
			cls._instances[cls] = super(MetaSingleton, \
				 cls).__call__(*args, **kwargs)
			print("there", cls._instances)
			return cls._instances[cls]

class Logger(metaclass=MetaSingleton):
	pass


logger1 = Logger()
logger2 = Logger()
# print("Logger1 -> ", logger1, "Logger2 -> ", logger2)