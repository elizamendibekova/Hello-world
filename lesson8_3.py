import csv
def csv_dict_writer(path,fieldnames, data):
	with open(path, "w") as out_file:
	writer = csv.DictWriter(out_file, delimiter=',', fieldnames=fieldnames)
	writer.writeheader()
	for row in data:
		writer.writerow(row)


data =[
	"first_name, last_name".split(","),
	"Ivan,Ivanov".split(','),
	"Petr,Petrov".split(','),
	"Klara,Korralova".split(',')
]

my_list =[]
fieldnames =data[0]

for values in data[1:]:
	inner_dict =dict(zip(fieldnames, values))
	my_list.append(inner.dict)

path = "dict_output.csv"
csv_dict_writer(path, fieldnames, my_list)