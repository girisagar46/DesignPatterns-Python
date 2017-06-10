# The  EventManager class is the Façade that simplifies the interface for  us
# EventManager  uses composition to create objects of the subsystems such as Hotelier ,  Caterer , and others
class EventManager(object):
	def __init__(self):
		print("EventManager: I will arrange all things\n")

	def arrange(self):
		self.hotelier = Hotelier()
		self.hotelier.bookHotel()

		self.florist = Florist()
		self.florist.setFlowerRequirements()

		self.caterer = Caterer()
		self.caterer.setCuisine()

		self.musican = Musican()
		self.musican.setMusicType()


# Hotelier, Florist, Musican, Caterer are all the subsytems that Facade will provide
class Hotelier(object):
	def __init__(self):
		print("Arranging the hotel for marriage? --")

	def __isavailable(self):
		print("Is hotel free for the day? -- ")
		available = False
		print("Hotel Status: ", available)

	def bookHotel(self):
		if self.__isavailable():
			print("Registered Booking\n\n")
		else:
			print("uh oh! hotel not available for the day!\n\n")

class Florist(object):
	def __init__(self):
		print("Flower decorations for the Event? -- ")

	def setFlowerRequirements(self):
		print("Some flowers are used for the decorations.")

class Caterer(object):
	def __init__(self):
		print("Food arrangements for the event? --")

	def setCuisine(self):
		print("Nepalese food will be served\n\n")

class Musican(object):
	def __init__(self):
		print("Music arrangements for the Event? --")

	def setMusicType(self):
		print("Lok dohori will be played in the ceremony.")


# You is the client that wants these arrangements
class You(object):
	def __init__(self):
		print("*** MAKE ALL THE ARRANGEMENTS FOR THE MARRIAGE CEREMONY ***")

	def askEventManager(self):
		print("Contacting the EventManager\n\n")
		em = EventManager()
		em.arrange()

	def __del__(self): # called after successfully creation of the object
		print("EventManager arranged all the things")

you = You()
you.askEventManager()