import csv
from bs4 import BeautifulSoup
import time
import re


#parse enzyme



soup = BeautifulSoup(open("C:\\Users\\snehal\\Desktop\\Drosophilla\\Drosophila\\OriginalFiles\\fly_protein_full.xml)"), "xml")
enzyme = soup.find_all("Protein")
temp = []
temp_syn = []
enzyme_result = []
syn_result = []
temp_go = []
go_result = []
temp_gene = []
gene_result = []
temp_location = []
location_result = []

for row in enzyme:
    if row.has_attr('ID'):
        temp.append(row['ID'].strip())
        temp[0] = temp[0].encode("utf-8")
        temp[0] = temp[0][4:]
        if row.find("common-name"):
            temp_syn.append(temp[0])
            temp_syn.append(row.find("common-name").string.strip().encode("utf-8"))




outFile = open("../DerivedFiles/enzyme.csv", "w")
writer = csv.writer(outFile)
writer.writerows(enzyme_result)
outFile.close()

outFile = open("../DerivedFiles/enzyme_synonym.csv", "w")
writer = csv.writer(outFile)
writer.writerows(syn_result)
outFile.close()

outFile = open("../DerivedFiles/enzyme_go.csv", "w")
writer = csv.writer(outFile)
writer.writerows(go_result)
outFile.close()

outFile = open("../DerivedFiles/enzyme_gene.csv", "w")
writer = csv.writer(outFile)
writer.writerows(gene_result)
outFile.close()

outFile = open("../DerivedFiles/enzyme_location.csv", "w")
writer = csv.writer(outFile)
writer.writerows(location_result)
outFile.close()

print("enzyme table done")
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()