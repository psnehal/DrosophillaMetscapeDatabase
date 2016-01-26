testDict = {"id.": "name"}
with open('EnzymeIDMapping.csv', 'r') as f:
        _ = next(f)
        _ = next(f)
        for line in f:
            splitLine = line.split("\t")
            testDict[int(splitLine[0])] = ",".join(splitLine[1:])