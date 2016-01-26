import csv
from bs4 import BeautifulSoup
import time
import re

start_time = time.time()
soup = BeautifulSoup(open('/home/snehal/Drosophila_Alla/onlineData/OriginalFiles/fly_compound_full.xml'), 'xml')
temp = [None]*9
compound_result = []
temp_left = []
temp_right = []
reaction_left = []
reaction_right = []
temp_syn = []
tempSysFin=[]

syn = []
count = 1
p = re.compile('<.*?>')
max=0
store= 0

for compound in soup.find_all('Compound', ID=True):
    #temp[0] = compound['frameid'].strip()

    temp[0] =  count

    if compound.find('molecule'):
        molecule = compound.find('molecule')
        if molecule.find('formula'):
            temp[2] = molecule.find('formula')['concise'].strip()
            #print temp[2]
            # print "\n from the formula loop"
    if compound.find('dblink'):
        db = compound.find_all('dblink')
        for item in db:
            db_type = item.find('dblink-db')
            db_id = item.find('dblink-oid')
            if db_type.string.strip() == 'CAS':
                temp[6] = db_id.string.strip()
            elif db_type.string.strip() == 'LIGAND-CPD':
                temp[3] = db_id.string.strip()
    if compound.find('synonym'):
        synonym = compound.find_all('synonym')
        for item in synonym:
            temp_syn.append(unicode(item.string.strip()).encode("utf-8"))
    if compound.find('inchi'):
        inchi = compound.find('inchi').string.strip().replace("InChI=", "")
        temp[4] = inchi
        max= len(inchi)
        if(store<max):
            store=max;


    if compound.find('molecular-weight'):
        mw = float(compound.find('molecular-weight').string.strip())
        temp[8] = mw
        temp[1] = int(mw)
    if compound.find('common-name'):
        primaryName = p.sub('',compound.find('common-name').string.strip())
        temp[5] = primaryName

    temp[7] = 5
print ("max is %s" %max)

