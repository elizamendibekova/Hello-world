text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec vulputate pellentesque vehicula. Pellentesque ornare pharetra nibh non tempus. Sed rhoncus fringilla sodales. Sed non tellus tempus, vulputate lorem vel, tempor ex. Fusce posuere accumsan augue, non sodales leo efficitur id. Nulla felis massa, bibendum vel velit quis, tincidunt eleifend lectus. Nulla semper, velit in aliquet facilisis, magna libero placerat nisl, in feugiat erat eros a leo. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Suspendisse potenti. Curabitur volutpat risus non leo dignissim porttitor. Etiam iaculis erat ut lacus commodo, nec congue augue consequat."

list = text.split()

file = open("C:\\Users\\Redmouse\\Desktop\\python\\lesson7\\text3.txt", "w")

for word in list:
	file.write(word + " ")

file.close()

file = open("C:\\Users\\Redmouse\\Desktop\\python\\lesson7\\text3.txt")

print(file.readline())