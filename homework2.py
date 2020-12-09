import random

while True:
	command = input("Скажи мудрость:\n")
	phrases = ["бла бла", "елка", "термос", "телефон", "игра"]

	if command == input("Скажи мудрость"):
		print(random.choice(phrases))
	elif command == "Знать нчего не хочу":
		print("Ok(((")
		continue
	elif command == "Выход":
		print("До свидания")
		break
	else:
		print("Неверный ввод")


