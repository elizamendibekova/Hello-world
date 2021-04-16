file= open("text.txt", "r")

#list_of_lines = [line.strip() for line in line]

#print(list_of_lines)

for line in file:
	print(line.strip())

