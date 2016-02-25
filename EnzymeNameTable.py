import csv
from bs4 import BeautifulSoup
import time
import re


enzDict = {"bid.": "id"}
with open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/Final/BioIDtoEnID.txt', 'r') as f:
        for line in f:
            splitLine = line.split("\t")
            #print splitLine[0]
            #print splitLine[1]
            #creating dictionary of enzyme biosyn id to the internal id of the enzyme table
            enzDict[(splitLine[2]).strip()] = splitLine[0]




#parse enzyme


synfile = open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/EnzymeNameTableSyn2.txt', 'w')
soup = BeautifulSoup(open("/home/snehal/Drosophila_Alla/onlineData/OriginalFiles/fly_protein_full.xml"), "xml")
enzyme = soup.find_all("Protein")
temp = [None]*5
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
count2=1
tempSynFin=[]
p = re.compile('<.*?>')

for row in enzyme:
    if row.has_attr('ID'):
        #print "count is ",count
        #temp[4] =
       # print ("id is ",temp[4])
        temp[0]= count
        bid=row['ID'].strip().encode("utf-8").replace("FLY:","")
        #print count
        if row.find("common-name"):
            primary_name=row.find("common-name").string.strip().encode("utf-8")
            temp[1]=primary_name
            #print "primary name ", primary_name
        temp[2]="primary"
        try:
            enid=enzDict[bid]
            temp[3]=enid
        except KeyError:
            print "Key could not find",bid
            temp[3]='none'
        temp[4]=bid
        if row.find("synonym"):
            synonym = row.find_all("synonym")
            for item in synonym:
                temp_syn.append(item.text.strip().encode("utf-8"))
        #print "length of temp_syn",len(temp_syn)
        #print "type of ",type(temp_syn)
        for index in range(len(temp_syn)):
            line=str(count2)+"\t"+ temp_syn[index]+"\t"+"synonyms"+"\t"+enid+"\n";
            synfile.write(line)


        #print temp
        enzyme_result.append(temp)
        temp = [None]*5
        tempSynFin=[]
        temp_syn=[]
        count+= 1
        count2+= 1


outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/EnzymeName3.csv", "w")
writer = csv.writer(outFile,lineterminator = '\n')
writer.writerows(enzyme_result)
outFile.close()


start_time = time.time()
print("enzyme table done")
print("--- %s seconds ---" % (time.time() - start_time))
