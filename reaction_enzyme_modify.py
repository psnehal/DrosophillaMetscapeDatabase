import csv

data = []
inFile = open("reaction_enzyme.csv", "rU")
reader = csv.reader(inFile)
for line in reader:
    line[1] = line[1].replace(" ", "")
    line[1] = line[1].replace("\n", "")
    line[1] = line[1].replace("T", "")
    data.append(line)
inFile.close()

temp = []
modified_data = []
for line in data:
    if line[1] == "":
        line[1] = "NULL"
    if len(line) > 3:
        for x in range(2, len(line)):
            temp.append(line[0])
            temp.append(line[1])
            temp.append(line[x])
            modified_data.append(temp)
            temp = []
    elif len(line) == 3:
        modified_data.append(line)
    else:
        temp.append(line[0])
        temp.append(line[1])
        temp.append("NULL")
        modified_data.append(temp)
        temp = []

outFile = open("reaction_enzyme_modified.csv", "wb")
writer = csv.writer(outFile)
writer.writerows(modified_data)
outFile.close()

