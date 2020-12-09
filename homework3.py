def calc():
	
	a = int(input("Please enter the first number:"))
	b = int(input("Please enter the second number:"))
	c = int(input("operation"))

	if operation == "+":
		print("{} + {} = " .format(number_1, number_2))
		print(number_1 + number_2)

	elif operation == "-":
		print("{} - {} = " .format(number_1, number_2))
		print(number_1 - number_2)

	elif operation == "*":
		print("{} * {} = " .format(number_1, number_2))
		print(number_1 * number_2)

	elif operation == "/":
		print("{} / {} = " .format(number_1, number_2))
		print(number_1 / number_2)

	else:
		print("You have typed a valid operator, please run the program again.")


def add(a, b):
	return a + b

def subtraction(a, b):
	return a - b

def multiply(a, b):
	return a * b

def division(a, b):
	return a / b


	

