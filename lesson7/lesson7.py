file = open('C:\\Users\\Redmouse\\Desktop\\python\\lesson7\\text.txt')
print(file.read(4))
print(file.read())

for line in file:
	print(line)