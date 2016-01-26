import csv
from bs4 import BeautifulSoup
import time
import re

soup = BeautifulSoup(open("/home/snehal/Drosophila_Alla/onlineData/OriginalFiles/fly_reaction_full.xml"), "xml")
reaction = soup.find_all("Reaction")
temp = [None]*4
reaction_result = []
temp_left = []
temp_right = []
reaction_left = []
reaction_right = []
temp_syn = []
reaction_synonym = []
temp_path = []
reaction_pathway = []
temp_enzyme = []
reaction_enzyme = []
count = 1
temp_reac=[]
reaction=[]

for row in reaction:
    if row.has_attr('ID'):
        temp[0] = count
        temp[1]= temp.append(row['ID'].strip().encode("utf-8").replace("FLY:",""))
        if row.find("reaction-direction"):
            reaction_direction = row.find("reaction-direction").string.strip()
            temp[2]= reaction_direction.encode("utf-8")
            print("direction",reaction_direction)
        if row.find("left"):
            left = row.find_all("left")
            for item in left:
                if item.find("Compound"):
                    temp_left.append(temp[0])
                    cpd = item.find("Compound")['frameid']
                    cpd = cpd.strip()
                    temp_left.append(cpd.encode("utf-8"))
                    if item.find("coefficient"):
                        temp_left.append(item.find("coefficient").string.strip())
                    else:
                        temp_left.append(1)

        if row.find("right"):
            right = row.find_all("right")
            for item in right:
                if item.find("Compound"):
                    temp_right.append(temp[0])
                    cpd = item.find("Compound")['frameid']
                    cpd = cpd.strip()
                    temp_right.append(cpd.encode("utf-8"))
                    if item.find("coefficient"):
                        temp_right.append(item.find("coefficient").string.strip())
                    else:
                        temp_right.append(1)

        temp_reac.append(count)
        temp_reac.append("|".join(temp_left))
        temp_left=[]
        temp_reac.append("|".join(temp_right))
        print("temp_react" ,temp_reac)
        temp_right=[]
        temp[3]=9
        reaction_result.append(temp)
        reaction.append(temp_reac)
        temp_reac=[]
        temp = [None]*4
        count+= 1


outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/reactionNew.csv", "wb")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(reaction_result)
outFile.close()

outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/reactiondirection.csv", "wb")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(reaction)
outFile.close()




start_time = time.time()
print("reaction table done")
print("--- %s seconds ---" % (time.time() - start_time))
