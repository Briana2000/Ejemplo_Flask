from typing import Protocol
from random import randint

class Doll(Protocol):
	"""	Doll Protocol
		Description:
			Protocol for Dolls
			A Protocol is a class that defines a set of methods
			that a class must implement.
			In easy words, a Protocol is an Interface.
		Attributes:
			_id : int
			_name : str
			_type : str
			_price : float
			_details : str
		Methods:
			__str__ : str
	"""
	_id : int
	_name : str
	_type : str
	_price : float
	_details : str
	def __str__():
		...

class FashionDoll(Doll):
	"""	FashionDoll Class
		Description:
			Class for Fashion Dolls that implements the Doll Protocol
		Attributes:
			_id : int
			_name : str
			_type : str
			_price : float
			_details : str
		Methods:
			__init__ : None
			__str__ : str
	"""
	def __init__(self, id : int = 0, Name : str = "", Type : str = "", price : float = 0.0, details : str = "") -> None:
		""" Constructor for FashionDoll Class
			Parameters:
				id : int
				Name : str
				Type : str
				price : float
				details : str
			Returns:
				None
			Description:
				Initializes the FashionDoll Class
				In case of no arguments, it will initialize the class with dumy values for testing
				if id is 0, it will generate a random id
				if price is not a float, it will cast it to float
		"""
		if id == 0:
			id = randint(1000, 9999)
		if Name == "":
			Name = "Dumy Name"
		if Type == "":
			Type = "Dumy Type"
		if price == 0.0:
			price = 0.0
		if details == "":
			details = "Dumy Details"
		self._id = id
		self._name = Name
		self._type = Type
		self._price = (float)(price) # Cast to float
		self._details = details

	def __str__(self) -> str:
		return f"ID: {self._id}\nName: {self._name}\nType: {self._type}\nPrice: {self._price}\nDetails: {self._details}"

if __name__ == "__main__":
	# generate a set of 5 dumy FashionDolls
	dolls = [ FashionDoll() for i in range(5) ]
	# print the details of each doll
	for doll in dolls:
		print(doll)
		print()