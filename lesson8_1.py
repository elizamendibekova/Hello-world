import csv

def csv_dict_reader(file_obj, delimiter=','):
	reader = csv.DictReader(file_obj, delimiter=delimiter)

	for line in reader:
		print(line)
		print("__________")
		print(line["first_name"])
		print(line["last_name"])
		print("__________")

with open("data.csv", "r") as file_obj:
	csv_dict_reader(f_obj)