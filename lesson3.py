def add(a, b):
	return a + b

def subtraction(a, b):
	return a - b

def multiply(a, b):
	return a * b

def division(a, b):
	return a / b

while True:
	a = input("Первое число:")
	b = input("Второе число:")
	c = input("Оператор:")

	if a.isdigit() and b.isdigit():
		a = float(a)
		b = float(b)

		if c == "+":
			print(add(a, b))
		elif c == "-":
			print(subtraction(a, b))
		elif c == "*":
			print(multiply(a, b))
		elif c == "/":
			print(division(a, b))
		else:
			print("Вы ввели не правильный Оператор")
	else:
		print("Вы ввели не число")


