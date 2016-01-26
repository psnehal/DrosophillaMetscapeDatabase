import csv
from bs4 import BeautifulSoup
import time
import re

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
coefficient=""
reaction_value=""


for row in reaction:
    if row.has_attr('ID'):
        temp[0] = count
        temp[1]= row['ID'].strip().encode("utf-8").replace("FLY:","")
        reaction_direction=""
        if row.find("reaction-direction"):
            reaction_direction = row.find("reaction-direction").string.strip().encode("utf-8")

        if row.find("left"):
            left = row.find_all("left")
            for item in left:
                if item.find("Compound"):
                    cpd = item.find("Compound")['frameid']
                    cpd = cpd.strip().encode("utf-8")
                    #print("CPd is in above left ",cpd)
                    if item.find("coefficient"):
                        coefficient=item.find("coefficient").string.strip()
                    cpd = coefficient+''+cpd
                    temp_left.append(cpd)
                    #print("CPd is in left ",cpd)
        #print("after the left",temp_left)
        coefficient=""
        if row.find("right"):
            right = row.find_all("right")
            for item in right:
                if item.find("Compound"):
                    cpd = item.find("Compound")['frameid']
                    cpd = cpd.strip().encode("utf-8")
                    if item.find("coefficient"):
                         coefficient=item.find("coefficient").string.strip()
                    cpd = coefficient.join(cpd)
                    temp_right.append(cpd)
        #print("after the right",temp_right)

        if temp_left:
            #reaction_left.append(temp_left)
            left_side='+'.join(temp_left)
            #temp_test.append(left_side)
            #print('temp_left',left_side)
        if temp_right:
            #reaction_right.append(temp_right)
            right_side='+'.join(temp_right)
            #temp_test.append(right_side)
            #print('temp_left',right_side)

        print("len of direction",reaction_direction)
        reaction_sample=''
        reaction_value=''
        if(reaction_direction == 'LEFT-TO-RIGHT'):
            reaction_sample = left_side + '=>'+ right_side
            reaction_value='false'
            print("left side loop" + reaction_sample )
        elif(reaction_direction == 'REVERSIBLE'):
            reaction_sample = left_side + '<=>'+ right_side
            reaction_value='true'
            print("reversible side loop"+ reaction_sample )
        elif(reaction_direction == 'RIGHT-TO-LEFT'):
            reaction_sample =  right_side+ '=>'+left_side
            reaction_value='false'
            print("right side loop" + reaction_sample )
        else:
            reaction_sample =  right_side+ '='+left_side
            reaction_value=''
            print"comes to the end",reaction_sample

        temp_test.append(count)
        temp_test.append('NAME')
        print("final sample" + reaction_sample )
        temp_test.append(reaction_sample)
        temp_test.append(count)

        temp[2]= reaction_value
        temp[3]=9
        #print("temp", temp_test)
        reaction_result.append(temp)
        reaction_test.append(temp_test)
        temp = [None]*4
        temp_left = []
        temp_right = []
        temp_test = []
        count+= 1



outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Reaction.csv", "wb")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(reaction_result)
outFile.close()

outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/ReactionEquation.csv", "wb")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(reaction_test)
outFile.close()



start_time = time.time()
print("reaction table done")
print("--- %s seconds ---" % (time.time() - start_time))
