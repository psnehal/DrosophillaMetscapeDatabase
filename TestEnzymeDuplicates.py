
eclist=[]
f= open('/home/snehal/Drosophila_Alla/SnehalScripts/finalFiles/EnzymeTable.txt')
for line in f:
    temp=line.split("\t")
    ecno=temp[1]
    eclist.append(ecno)


def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )

print list_duplicates(eclist)



print '1.3.1.385656' in eclist