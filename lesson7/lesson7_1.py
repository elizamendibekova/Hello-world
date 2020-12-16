list = [str(i) + str(i-1) for i in range(10)]

file = open("C:\\Users\\Redmouse\\Desktop\\python\\lesson7\\text2.txt", "w")

for i in list:
	file.write(i + "\n")

file.close()

file = open("C:\\Users\\Redmouse\\Desktop\\python\\lesson7\\text2.txt", "r")
#list = [line.strip() for line in file]

file.readline()
file.readline()
file.readline()

print(file.tell())

file.seek(1)
print(file.tell())