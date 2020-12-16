from abc import ABC, abstractmethod

class ChessPiece(ABC):
	def draw(self):
		print("Drew a chess piece")

	@abstractmethod
	def move(self):
		pass

class Queen(ChessPiece):
	def move(self):
		print("Moved Queen to e2e4")

q = Queen()
q.draw()
q.move()

