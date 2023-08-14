from typing import Protocol

class Doll(Protocol):
	"""	Doll Protocol
		Description:
			Protocol for Dolls
			A Protocol is a class that defines a set of methods
			that a class must implement.
			In easy words, a Protocol is an Interface.
		Attributes:
			Name : str
			Type : str
			Price : float
			Details : str
		Methods:
			__str__ : str
	"""
	Name : str
	Type : str
	Price : float
	Details : str
	def __str__():
		...

class FashionDoll(Doll):
	"""	FashionDoll Class
		Description:
			Class for Fashion Dolls that implements the Doll Protocol
		Attributes:
			Name : str
			Type : str
			Price : float
			Details : str
		Methods:
			__init__ : None
			__str__ : str
	"""
	def __init__(self, name:str, Type:str, price : float, details:str) -> None:
		self.Name = name
		self.Type = Type
		self.Price = (float)(price) # Cast to float
		self.Details = details

	def __str__(self) -> str:
		return f"Name: {self.Name}, Type: {self.Type}, Price: {self.Price}, Details: {self.Details}"

if __name__ == "__main__":
	doll = FashionDoll("Barbie", "Fashion Doll", 1000, "Pink Dress")
	print(doll)