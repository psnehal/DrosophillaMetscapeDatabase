testDict = {"id.": "name"}
with open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/EnzymeIDMapping.csv', 'r') as f:
        for line in f:
            splitLine = line.split("\t")
            #print splitLine[0]
            #print splitLine[1]
            testDict[(splitLine[1]).strip()] = splitLine[0]




print 'MONOMER54L-3156' in testDict


proteinid =[]

synfile = open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/ecnotoenzymeidmappingwithoutnone.txt', 'w')
f= open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/reactionEnzymeMod.csv')
for line in f:
    print line,
    temp=line.split(",")
    reactionid=temp[0]
    ecno=temp[1].replace("EC-","")
    proteinid = temp[2].split("|")
    if(ecno != "none"):
        for index in range(len(proteinid)):
            if(bool(proteinid[index] and proteinid[index].strip())):
                print "true"
                check = proteinid[index].strip()
                print check
                mapping=testDict[check]
                print "mapping ",mapping
                line = mapping+"\t"+ecno+"\t"+"9"+"\n"
                print line
                synfile.write(line)
            else:
                print "empty string \n"


