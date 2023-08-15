from typing import Protocol
from random import randint
#from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()


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

class FashionDoll(Doll):#, db.Model):
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
	''' DataBase Model
	__tablename__ = 'fashion_dolls'
	_id = db.Column(db.Integer, primary_key=True)
	_name = db.Column(db.String(255), nullable=False)
	_type = db.Column(db.String(255))
	_price = db.Column(db.Float, nullable=False)
	_details = db.Column(db.Text)
	'''
	def __init__(self, * , ID : int = 0, Name : str = "", Type : str = "", Price : float = 0.0, Details : str = "") -> None:
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
		if ID == 0:
			ID = randint(1000, 9999)
		if Name == "":
			Name = "Dumy Name"
		if Type == "":
			Type = "Dumy Type"
		if Price == 0.0:
			Price = 0.0
		if Details == "":
			Details = "Dumy Details"
		self._id = ID
		self._name = Name
		self._type = Type
		self._price = (float)(Price) # Cast to float
		self._details = Details

	def __str__(self) -> str:
		return f"ID: {self._id}\nName: {self._name}\nType: {self._type}\nPrice: {self._price}\nDetails: {self._details}"
	@property
	def id(self) -> int:
		return self._id
	@property
	def name(self) -> str:
		return self._name
	@property
	def type(self) -> str:
		return self._type
	@property
	def price(self) -> float:
		return self._price
	@property
	def details(self) -> str:
		return self._details
	@id.setter
	def id(self, id : int) -> None:
		self._id = id
	@name.setter
	def name(self, Name : str) -> None:
		self._name = Name
	@type.setter
	def type(self, Type : str) -> None:
		self._type = Type
	@price.setter
	def price(self, price : float) -> None:
		self._price = price
	@details.setter
	def details(self, details : str) -> None:
		self._details = details

if __name__ == "__main__":
	# generate a set of 5 dumy FashionDolls
	dolls = [ FashionDoll() for i in range(5) ]
	# print the details of each doll
	for doll in dolls:
		print(doll)
		print()