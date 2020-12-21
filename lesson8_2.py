import csv

def to_csv_writer(data, path):
	with open(path, "w") as csv_file:
		csv_writer = csv.writer(csv_file, delimeter="/")
		for line in data:
			csv_writer.writerow(line)


data = ["first_name,last_name". split(","),
		"Ivan,Ivanov".split(","),
		 "Petr,Petrov".split(","),
		 "Klara,Korallova".split(",")]

path = "C:\\Users\\Redmouse\\Desktop\\python\\lesson9\\output.csv"
to_csv_writer(data, path)
