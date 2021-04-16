import csv

def csv_reader(file_obj):
	reader = csv.reader(file_obj)
	for row in reader:
		print(" ".join(row))

csv_path = "TB_data_dictionary_2021-04-12.csv"

with open(csv_path, "r") as f_obj:
	csv_reader(f_obj)