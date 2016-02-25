import csv
from bs4 import BeautifulSoup
import time




soup = BeautifulSoup(open("/home/snehal/Drosophila_Alla/onlineData/OriginalFiles/fly_gene_full.xml"), "xml")
enzyme = soup.find_all("Gene")
temp = [None]*3
gene_result = []
temp_proteins=[]
temp_syn=[]
db_id=''


for row in enzyme:
    if row.has_attr('ID'):
        temp[0] = row['ID'].strip()
        temp[0] = temp[0].encode("utf-8")
        id = temp[0].replace("FLY:","")
        if row.find("product"):
            enzymes = row.find("product")
            for item in enzymes.find_all('Protein'):
                temp_proteins.append(item['frameid'].strip())
                print item['frameid'].strip()
        if row.find("common-name"):
            name = row.find("common-name").string.strip().encode("utf-8")
        else:
            temp[1] = ''
        if row.find('dblink'):
              db = row.find_all('dblink')
              for item in db:
                  db_id = item.find('dblink-oid').string.strip()
        if row.find("synonym"):
            synonym = row.find_all("synonym")
            for item in synonym:
                temp_syn.append(item.string.strip().encode("utf-8"))
        if temp_proteins:
            temp[0]=id
            temp[1]=db_id
            temp[2]="|".join(temp_proteins)
            gene_result.append(temp)
        temp = [None]*3
        temp_proteins=[]

outFile = open("/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/geneBioCynToEnzyme2.csv", "w")
writer = csv.writer(outFile,delimiter='\t',lineterminator = '\n')
writer.writerows(gene_result)
outFile.close()