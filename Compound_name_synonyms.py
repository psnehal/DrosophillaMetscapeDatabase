import csv
from bs4 import BeautifulSoup
import time
import re
temp = []
count = 4857
f= open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/synonymstab.csv')
prifile = open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/compoundpPrimaryName.txt', 'w')
synfile = open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/compoundpSynonymsName.txt', 'w')
for line in f:
    print line,
    temp=line.split("\t")
    #print temp[0]
    #print temp [1]
    #print temp[2].replace("\n","").split(";")
    syn = temp[2].replace("\n","").split("|")
    linep = temp[0]+"\t"+temp[1]+"\t"+"primary"+"\t"+temp[0]+"\n"
    print "primary compound is" , linep
    prifile.write(linep)
    for index in range(len(syn)):
        if(bool(syn[index] and syn[index].strip())):
            print "true"
            p = re.compile(r'<.*?>')
            synonym=p.sub('', syn[index])
            line = str(count)+"\t"+synonym+"\t"+"synonym"+"\t"+temp[0]+"\n"
            print line
            count += 1
            synfile.write(line)


        else:
            print "empty string \n"
            syn[index]











