import sqlite3

"""
Points to be taken care of:
Consistency across operations in the database—one operation shouldn’t result in conflicts with other operations
Memory and CPU utilization should be optimal for the handling of multiple operations on the database
"""


class MetaSingleton(type):
	_instances = {}
	def __call__(cls, *args, **kwargs):
		if cls not in cls._instances:
			cls._instances[cls] = super(MetaSingleton, \
				cls).__call__(*args, **kwargs)
		return cls._instances[cls]


class Database(metaclass = MetaSingleton):
	connection = None
	def connect(self):
		if self.connection is None:
			self.connection = sqlite3.connect("db.sqlite3")
			self.cursorobj = self.connection.cursor()
		return self.cursorobj

db1 = Database().connect()
db2 = Database().connect()

print("Database Objects DB1", db1)
print("Database Objects DB2", db2)

# OUTPUT:
# Database Objects DB1 <sqlite3.Cursor object at 0x7fd396b3c490>
# Database Objects DB2 <sqlite3.Cursor object at 0x7fd396b3c490>
