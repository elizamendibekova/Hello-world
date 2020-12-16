from abc import ABC, abstractmethod

class Basic(ABC):
	@abstractmethod
	def hello(self):
		print("Hello from Basic class")

class Advanced(Basic):
	def hello(self):
		print("hi")
		super().hello()

class Second(Basic):
	def hello(self):
		super.hello()
	
a = Advanced()
a.hello()

s = Second()
s.hello()