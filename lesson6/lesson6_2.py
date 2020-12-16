class Donkey:
	def say(self):
		print("I'm donkey")

	def walk(self):
		print("fjkghdig")

class Horse:
	def say(self):
		print(" I'm horse")

	def run(self):
		print("jhgjhkj")


class Moul(Donkey, Horse):
	def hi(self):
		print("Hi")

	def say(self):
		print("I'm moul")

donkey = Donkey()
horse = Horse()
moul = Moul()

donkey.say()
horse.say()
moul.hi()

moul.say()
moul.walk()
moul.run()