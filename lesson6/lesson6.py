class A:
	def _print_private(self):
		print("Это приватный метод")

a = A()
a._print_private()

class B:
	def __print_very_private(self):
		print("то очень приватный код")

b = B()
# b.__print_very_private()

b._B__print_very_private()