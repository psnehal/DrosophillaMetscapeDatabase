import csv
from bs4 import BeautifulSoup
import time
import re

compDict = {"id.": "name"}
with open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Final/compoundIDToNameMapping.csv', 'r') as f:
        for line in f:
            splitLine = line.split(",")
            #print splitLine[0]
            #print splitLine[1]
            #creating dictionary of compound biosyn id to the primary name inn the table
            compDict[(splitLine[1]).strip()] = splitLine[2]

compReactDict = {"bioid.": "id"}
with open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Final/compoundIDToNameMapping.csv', 'r') as f:
        for line in f:
            splitLine = line.split(",")
            #print splitLine[0]
            #print splitLine[1]
            #creating dictionary of compound biosyn id to the primary name inn the table
            compReactDict[(splitLine[1]).strip()] = splitLine[0]

print "from the dict",compReactDict

soup = BeautifulSoup(open("/home/snehal/Drosophila_Alla/onlineData/OriginalFiles/fly_reaction_full.xml"), "xml")
reaction = soup.find_all("Reaction")
temp = [None]*4
temp_test=[]
reaction_result = []
reaction_test = []
temp_left = []
temp_right = []
reaction_left = []
reaction_right = []
reaction_enzyme = []
count = 1
coefficient=1
reaction_value=""
temp_path=[]
temp_path_all=[]
reaction_pathway=[]
temp_com2reac=[]
com2reac=[]
com2in=[]
com2out=[]
temp_com2in=[]
temp_com2out=[]


for row in reaction:
    if row.has_attr('ID'):
        temp[0] = count
        temp[1]= row['ID'].strip().encode("utf-8").replace("FLY:","")
        testid=row['ID'].strip().encode("utf-8").replace("FLY:","")
        reaction_direction=""
        if row.find("reaction-direction"):
            reaction_direction = row.find("reaction-direction").string.strip().encode("utf-8")

        if row.find("left"):
            left = row.find_all("left")
            for item in left:
                if item.find("Compound"):
                    cpd = item.find("Compound")['frameid']
                    cpd = cpd.strip().encode("utf-8")
                    compbioid= cpd.replace('\n','')
                    fcpd= compDict[compbioid].replace('\n','')#maps biocyn id to the name
                    compid=compReactDict[compbioid]#maps biocid to the id in compound table
                    #print("CPd is in above left ",fcpd)
                    if item.find("coefficient"):
                        coefficient=item.find("coefficient").string.strip()
                    temp_com2reac.append(compid)
                    temp_com2reac.append(count)
                    temp_com2reac.append(coefficient)
                    temp_com2reac.append("true")
                    fcpd = str(coefficient)+fcpd
                    temp_left.append(fcpd)
                    com2reac.append(temp_com2reac)
                    temp_com2reac=[]
                    print("CPd is in left ",cpd)
        #print("after the left",temp_left)

        coefficient="1"
        if row.find("right"):
            right = row.find_all("right")
            for item in right:
                if item.find("Compound"):
                    cpd = item.find("Compound")['frameid']
                    cpd = cpd.strip().encode("utf-8")
                    compbioid= cpd.replace('\n','')
                    fcpd= compDict[compbioid].replace('\n','')
                    compid=compReactDict[compbioid]#maps biocid to the id in compound table
                    if item.find("coefficient"):
                         coefficient=item.find("coefficient").string.strip()
                    temp_com2reac.append(compid)
                    temp_com2reac.append(count)
                    temp_com2reac.append(coefficient)
                    temp_com2reac.append("true")
                    fcpd = str(coefficient)+fcpd
                    com2reac.append(temp_com2reac)
                    temp_com2reac=[]
                    #maps id to the name
                    temp_right.append(fcpd)
        #print("after the right",temp_right)

        if temp_left:
            #reaction_left.append(temp_left)
            left_side='+'.join(temp_left)
            temp_com2in.append(count)
            temp_com2in.append(left_side)
            com2in.append(temp_com2in)
            #temp_test.append(left_side)
            #print('temp_left',left_side)
        if temp_right:
            #reaction_right.append(temp_right)
            right_side='+'.join(temp_right)
            temp_com2out.append(count)
            temp_com2out.append(right_side)
            com2out.append(temp_com2out)
            #temp_test.append(right_side)
            #print('temp_left',right_side)
        if row.find("in-pathway"):
            pathway = row.find_all("in-pathway")
            #print "reaction id",row['ID'].strip().encode("utf-8").replace("FLY:","")
            for item in pathway:
                if item.find("Pathway"):
                    pathway_id = item.find_all("Pathway")
                    #print len(pathway_id)
                    for item2 in pathway_id:
                        pathway_id2 = item2['frameid'].strip()
                        pathway_id2=pathway_id2.encode("utf-8")
                        #print pathway_id2
                        temp_path.append(pathway_id2)


        temp_path_all.append(count)
        temp_path_all.append(testid)
        #print ("temp_path",temp_path)
        complete_pathway = "|".join(temp_path)

        temp_path_all.append(complete_pathway)

        reaction_sample=''
        reaction_value=''
        if(reaction_direction == 'LEFT-TO-RIGHT'):
            reaction_sample = left_side + '=>'+ right_side
            reaction_value='false'
            #print("left side loop" + reaction_sample )
        elif(reaction_direction == 'REVERSIBLE'):
            reaction_sample = left_side + '<=>'+ right_side
            reaction_value='true'
            #print("reversible side loop"+ reaction_sample )
        elif(reaction_direction == 'RIGHT-TO-LEFT'):
            reaction_sample =  right_side+ '=>'+left_side
            reaction_value='false'
            #print("right side loop" + reaction_sample )
        else:
            reaction_sample =  right_side+ '='+left_side
            reaction_value=''
            #print"comes to the end",reaction_sample
        if len(reaction_sample)==0:
            print "found 0 for reaction sample"
        temp_test.append(count)
        temp_test.append('NAME')
        #print("final sample" + reaction_sample )
        temp_test.append(reaction_sample)
        temp_test.append(count)

        temp[2]= reaction_value
        temp[3]=9
        #print("temp", temp_test)
        reaction_result.append(temp)
        reaction_test.append(temp_test)
        if len(temp_path)>0:
            reaction_pathway.append(temp_path_all)


        temp = [None]*4
        temp_left = []
        temp_right = []
        temp_test = []
        temp_path=[]
        temp_path_all=[]
        temp_com2in=[]
        temp_com2out=[]

        count+= 1



outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Reaction12.csv", "wb")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(reaction_result)
outFile.close()

outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/ReactionEquation12.csv", "wb")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(reaction_test)
outFile.close()

outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Reaction2Pathway.csv", "wb")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(reaction_pathway)
outFile.close()

outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Compound2Reaction.csv", "wb")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(com2reac)
outFile.close()


outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Compound2InputsREaction.csv", "wb")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(com2in)
outFile.close()


outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Compound2OutputsReaction.csv", "wb")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(com2out)
outFile.close()


start_time = time.time()
print("reaction table done with count" , testid)
print("--- %s seconds ---" % (time.time() - start_time))
