i = open("01mapper_output.txt","r")  # open file, read-only
s = open("sorter_output.txt", "w") # open file, write
lines = i.readlines()
lines.sort()

for line in lines:
	s.write(line)
i.close()
s.close()
