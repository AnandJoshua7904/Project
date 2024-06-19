with open("Anand.txt", "r") as file:
	data = file.readlines()
	for line in data[:2]:
		# word = line.split()
		print (line,end="")