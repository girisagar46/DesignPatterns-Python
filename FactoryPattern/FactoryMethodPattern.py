"""
1. We define an interface to create objects, but instead of the factory 
being responsible for the object creation, the responsibility 
is deferred to the subclass that decides the class to be instantiated.
2. The Factory method creation is through inheritance and not through instantiation.
3. The Factory method makes the design more customizable. It can return the same
instance or subclass rather than an object of a certain type (as in the simple factory
method).
"""

from abc import ABCMeta , abstractmethod

class Section(metaclass = ABCMeta):
	@abstractmethod
	def describe(self):
		pass

class PersonalSection(Section):
	def describe(self):
		print("Personal Section")

class AlbumSection(Section):
	def describe(self):
		print("Album Section")

class PatentSection(Section):
	def describe(self):
		print("Patent Section")

class PublicationSection(Section):
	def describe(self):
		print("Publication Section")


class Profile(metaclass = ABCMeta):
	def __init__(self):
		self.sections = []
		self.createProfile()
	@abstractmethod
	def createProfile(self):
		pass

	def getSections(self):
		return self.sections
	def addSection(self, section):
		self.sections.append(section)


class Linkedin(Profile):
	def createProfile(self):
		self.addSection(PersonalSection())
		self.addSection(PatentSection())
		self.addSection(PublicationSection())

class Facebook(Profile):
	def createProfile(self):
		self.addSection(PersonalSection())
		self.addSection(AlbumSection())

if __name__ == '__main__':
	profile_type = input("Which profile to create? [Facebook or Linkedin]")
	profile = eval(profile_type)()
	print("Creating profile for...", type(profile).__name__)
	print("Profile has sections...", profile.getSections())