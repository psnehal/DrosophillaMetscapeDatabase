

genefile = open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/GeneFile.txt', 'w')
namefile = open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/EntrezToFlyBase.txt', 'w')

f= open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/drosophilla_gene.txt')
count=1
for line in f:
    temp=line.split("\t")
    entId= temp[0]
    taxid=temp[1]
    flyid=temp[2]
    name=temp[3]
    line3=str(count)+"\t"+taxid+"\t"+flyid+"\t"+name+"\n"
    genefile.write(line3)
    line2=str(count)+"\t"+entId+"\t"+flyid+"\n"
    namefile.write(line2)
    count=count+1



geneDict = {"id.": "name"}
with open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/GeneFile.txt', 'r') as f:
        for line in f:
            splitLine = line.split("\t")
            #print len(splitLine)
            #print splitLine[1]
            #creating dictionary of compound biosyn id to the primary name inn the table
            if len(splitLine)== 4:
                geneDict[(splitLine[2]).strip().upper()] = splitLine[0]
print geneDict
print "got the geneid from dict",geneDict['FBGN0004172']

enzDict = {"bioid.": "id"}
with open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/EnzymeName2.csv', 'r') as f:
        for line in f:
            splitLine = line.split(",")
            #print splitLine[0]
            #print splitLine[1]
            #creating dictionary of compound biosyn id to the primary name inn the table
            enzDict[(splitLine[4]).strip()] = splitLine[3]

print "got the enzDict from dict",enzDict['FBGN0085605-MONOMER']



genefile = open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Gene2ReactionIdMissing.txt', 'w')
#namefile = open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/EnzymesNotFOund.txt', 'w')
final = open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Gene2Reaction.txt', 'w')
#f= open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/geneBioCynToEnzyme.csv')
f= open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/geneBioCynToEnzyme.csv')
count=1
geneid=''
enzId=''

for line in f:
    temp=line.split("\t")
    genebid=temp[0]
    enzBid=temp[1]
    #print "input the geneid",enzBid.strip(),"check"
    try:
        geneid=geneDict[genebid]
        enzid=enzDict[enzBid.strip()]
        if enzid:
            line4=geneid+"\t"+enzid+"\n"
            print "got the geneid"+enzid
            final.write(line4)
    except KeyError:
        genefile.write(geneid+"\t"+enzBid.strip()+"\n")






