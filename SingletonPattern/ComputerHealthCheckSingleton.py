class HealthCheck(object):
	_instances = None
	def __new__(cls, *args, **kwargs): # cls deals with the class itself
		if not HealthCheck._instances: # check if objetc exists
			HealthCheck._instances = super(HealthCheck, \
				cls).__new__(cls, *args, **kwargs) # create new object and assign to the instance variable _instances
		return HealthCheck._instances # return the same object if instantiated again

	def __init__(self):
		self._servers = []


	def addServer(self):
		self._servers.append("Server 1")
		self._servers.append("Server 2")
		self._servers.append("Server 3")
		self._servers.append("Server 4")

	def changeServer(self):
		self._servers.pop() # remove the last server
		self._servers.append("Server 5")


# hc1 and hc2 both are same object

hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.addServer()
print("Schedule health check for HC1...")
for i in range(4):
	print("Checking", hc1._servers[i])


hc2.changeServer()
print("Schedule health check for HC2...")
for i in range(4):
	print("Checking", hc2._servers[i])