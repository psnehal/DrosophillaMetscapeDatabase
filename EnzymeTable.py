




#this table read from the reactionEnzymeMod file which contains mapping of reaction name to ec number to multiple enzyme names.
#So Enzyme tablw will have all exnumber and mappied to unique id. Which then will be mapped to the name in EnzymeName table in EnzymeNameTable.
#EnzymeNameTOBioId contains mapping of bioid to the command names. Which will be added to EnzymeName table

proteinid =[]
eclist=[]
count =1;
synfile = open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/EnzymeTable1.txt', 'w')
namefile = open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/BioIDtoEnID1.txt', 'w')
f= open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/old/reactionEnzymeMod.csv')
for line in f:
    #print line,
    temp=line.split(",")
    reactionid=temp[0]
    ecno=temp[1].replace("EC-","")

    proteinid = temp[2].split("|")
    if(ecno != "none"):
        if ecno not in eclist:
            eclist.append(ecno)
            line = str(count)+"\t"+ecno+"\t"+"9"+"\n"
            synfile.write(line)
            for index in range(len(proteinid)):
                if(bool(proteinid[index] and proteinid[index].strip())):
                    #print "true"
                    check = proteinid[index].strip()
                    #enzId ecno proteinBioId
                    line2=str(count)+"\t"+ecno+"\t"+check+"\n"
                    #print line
                    namefile.write(line2)
                else:
                    print "empty string \n"
            count=count+1
        else:
            print "duplicate key",ecno





