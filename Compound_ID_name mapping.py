import csv
from bs4 import BeautifulSoup
import time
import re

start_time = time.time()
soup = BeautifulSoup(open('/home/snehal/Drosophila_Alla/onlineData/OriginalFiles/fly_compound_full.xml'), 'xml')
temp = [None]*3
compound_result = []



syn = []
count = 1
p = re.compile('<.*?>')

for compound in soup.find_all('Compound', ID=True):
    #temp[0] = compound['frameid'].strip()

    temp[0] =  count
    id = compound['frameid'].strip()
    temp[1]=id;
    if compound.find('common-name'):
        primaryName = p.sub('',compound.find('common-name').string.strip())
        temp[2] = primaryName
        print primaryName
    compound_result.append(temp)
    temp = [None]*3
    count+= 1
    #print ("end of the loop with count is %s", count)

with open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/compoundIDToNameMapping.csv', 'w') as compound_file:
    writer = csv.writer(compound_file, lineterminator = '\n')
    writer.writerows(compound_result)

print("compound id mapping table from snehal script is done")
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()