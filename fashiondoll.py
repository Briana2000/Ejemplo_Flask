from typing import Protocol

class Doll(Protocol):
	Name : str
	Type : str
	Price : float
	Details : str
	def __str__():
		...

class FashionDoll(Doll):
	def __init__(self, name, type, price, details):
		self.Name = name
		self.Type = type
		self.Price = (float)(price)
		self.Details = details

	def __str__(self):
		return f"Name: {self.Name}, Type: {self.Type}, Price: {self.Price}, Details: {self.Details}"

if __name__ == "__main__":
	doll = FashionDoll("Barbie", "Fashion Doll", 1000, "Pink Dress")
	print(doll)