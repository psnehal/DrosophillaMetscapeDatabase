pathDict = {"biocynid.": "id"}
with open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Final/pathway.tab', 'r') as f:
        for line in f:
            splitLine = line.split("\t")
            pathDict[(splitLine[2]).strip()] = splitLine[0]





pathway=[]
recpathfile = open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/reactiontopathway.tab', 'w')
f= open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Final/Reaction2PathwayBiCynID.csv')

for line in f:
    #print line,
    temp=line.split(",")
    reactid = temp[0]
    pathways=temp[1].split("|")
    print(len(pathways))
    if len(pathways)>1:
        for index in range(len(pathways)):
            pathway=pathways[index].replace("\n",'')
            print "in loop",pathway
            try:
                pathid= pathDict[pathway]
            except KeyError:
                print "Key could not find",pathway
            line=reactid+"\t"+pathid+"\n"
            recpathfile.write(line)
    else:
        pathway=pathways[0].replace("\n",'')
        print "notn loop",pathways[0].replace("\n",'')
        try:
            pathid= pathDict[pathway]
        except KeyError:
            print "Key could not find",pathway
        line=reactid+"\t"+pathid+"\n"
        recpathfile.write(line)





