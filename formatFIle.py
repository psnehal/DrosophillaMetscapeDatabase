synfile = open('/home/snehal/DataFiles/LRpath/bhc80Mod.txt', 'w')
f= open('/home/snehal/DataFiles/LRpath/bhc80.txt')
for line in f:
    temp=line.split("\t")
    print len(temp[0].strip()), 'with value', temp[0]
    print temp[1]
    print temp[2]
    line = temp[0].strip()+"\t"+temp[1]+"\t"+temp[2]+"\n"
    synfile.write(line)