compDict = {"id.": "name"}
with open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/compoundIDToNameMapping.csv', 'r') as f:
        for line in f:
            splitLine = line.split(",")
            #print splitLine[0]
            #print splitLine[1]
            #creating dictionary of compound biosyn id to the primary name inn the table
            compDict[(splitLine[1]).strip()] = splitLine[2]




print 'MONOMER54L-3156' in compDict

import re




proteinid =[]

synfile = open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/REactionEquationWithCompoundId', 'w')
f= open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Final/ReactionEquation.csv')
for line in f:
    print line,
    temp=re.split('+ \= \=> \<=>',line)
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