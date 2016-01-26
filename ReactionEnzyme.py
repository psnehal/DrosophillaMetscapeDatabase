import csv
from bs4 import BeautifulSoup
import time


#this script creates the enzyme name/id to exnumber mapping which will be used to create enzyme table


soup = BeautifulSoup(open("/home/snehal/Drosophila_Alla/onlineData/OriginalFiles/fly_reaction_full.xml"), "xml")
reaction = soup.find_all("Reaction")
temp = []
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
pro=[]

for row in reaction:
    if row.has_attr('ID'):
        temp.append(row['ID'].strip())
        temp[0] = temp[0].encode("utf-8")
        temp[0] = temp[0][4:]
        temp_enzyme.append(temp[0])
        print"reaction id", temp[0]
        ec_number='none'
        if row.find("ec-number"):
            ec_number = row.find("ec-number").text.strip()
            print len(ec_number.split( )[0])

            #print 'temp_enzyme', ec_number.split( )[0]
        temp_enzyme.append( ec_number.split( )[0])
        if row.find("enzymatic-reaction"):
            enzymatic_reaction = row.find_all("Enzymatic-Reaction")
            for item in enzymatic_reaction:
                if item.find("Protein"):
                    protein = item.find("Protein")
                    pro.append(protein['frameid'].strip().encode("utf-8"))
                    #print 'protein',protein['frameid'].strip().encode("utf-8")
        proteins='|'.join(pro)
        #print "protein length is", len(protein)
        print 'proteins',proteins
        temp_enzyme.append(proteins)
        temp = []
        pro=[]
        if temp_enzyme:
            print "temp_enzyme",(temp_enzyme)
            if(len(temp_enzyme)==1):
                print "with just 1", temp_enzyme
            reaction_enzyme.append(temp_enzyme)
            temp_enzyme = []


outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/reactionEnzymeMod.csv", "w")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(reaction_enzyme)
outFile.close()
start_time = time.time()
print("reaction enzyme table done")
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()