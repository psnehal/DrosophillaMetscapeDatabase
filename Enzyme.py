import csv
from bs4 import BeautifulSoup
import time
import re



#parse enzyme



soup = BeautifulSoup(open("/home/snehal/Drosophila_Alla/onlineData/OriginalFiles/fly_protein_full.xml"), "xml")
enzyme = soup.find_all("Protein")
temp = [None]*4
temp_syn = []
enzyme_result = []
syn_result = []
temp_go = []
go_result = []
temp_gene = []
gene_result = []
temp_location = []
location_result = []
count=1
tempSynFin=[]
p = re.compile('<.*?>')

for row in enzyme:
    if row.has_attr('ID'):
        #print "count is ",count
        #temp[4] = row['ID'].strip().encode("utf-8").replace("FLY:","")
       # print ("id is ",temp[4])
        temp[0]= count
        #print count
        if row.find("common-name"):
            primary_name=row.find("common-name").string.strip().encode("utf-8")
            temp[1]=primary_name
            print "primary name ", primary_name
        if row.find("synonym"):
            synonym = row.find_all("synonym")
            for item in synonym:
                temp_syn.append(item.text.strip().encode("utf-8"))
        #print "length of temp_syn",len(temp_syn)
        #print "type of ",type(temp_syn)
        if len(temp_syn) == 0:
            synonyms=""
        elif(len(temp_syn) == 1):
            synonyms=temp_syn[0]
        else:
            synonyms = '|'.join(temp_syn)
        if temp_syn:
            tempSynFin.append(count)
            tempSynFin.append(primary_name)
            tempSynFin.append(synonyms)
            syn_result.append(tempSynFin)
            temp_syn = []
        temp[2]="primary"
        temp[3]=count

        #print temp
        enzyme_result.append(temp)
        temp = [None]*4
        tempSynFin=[]
        temp_syn=[]
        count+= 1


outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/EnzymeName.csv", "w")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(enzyme_result)
outFile.close()

outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/EnzymeSynonyms.csv", "w")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(syn_result)
outFile.close()

start_time = time.time()
print("enzyme table done")
print("--- %s seconds ---" % (time.time() - start_time))
