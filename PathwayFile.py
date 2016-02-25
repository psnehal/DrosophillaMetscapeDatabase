import csv
from bs4 import BeautifulSoup
import time
import re


#parse pathway
soup = BeautifulSoup(open("/home/snehal/Drosophila_Alla/onlineData/OriginalFiles/fly_pathway_full.xml"), "xml")
enzyme = soup.find_all("Pathway")
temp = [None]*4
pathway_result = []
count = 1
p = re.compile('<.*?>')

for row in enzyme:
    if row.has_attr('ID'):
        temp[0] = count
        id=row['ID'].strip()
        id=id.encode("utf-8").replace("FLY:","")
        temp[2]=id
        if row.find("common-name"):
            name = row.find("common-name").string.strip().encode("utf-8")
            temp[1] =p.sub('',name)
        else:
            temp[1] = ''
        temp[3]=9
        pathway_result.append(temp)
        temp = [None]*4
        count+= 1

outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/pathway.tab", "w")
writer = csv.writer(outFile,delimiter='\t')
writer.writerows(pathway_result)
outFile.close()

print("pathway table done")
