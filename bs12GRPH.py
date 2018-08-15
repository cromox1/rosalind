__author__ = 'cromox'

def inputfile(filename):
    with open(filename) as f:
        xx = f.read().replace('\n','').split('>')
        f.close()
    return xx

def dict_fastaformat(seqsfasta):
    dctdata = {}
    for seq in seqsfasta:
        if len(seq) > 0:
            for i in range(len(seq)):
                try:
                    y = int(seq[i-1])
                    x = seq[i]
                    if type(y) == int and x in 'ACGT':
                        div1 = i
                except:
                    pass
            if div1 > 0:
                key = seq[:div1]
                value = seq[div1:]
                dctdata[key] = value
    return dctdata

def carikey(dict, value):
    for k,v in dict.items():
        if v == value:
            return k

def overlapstring(dictdata, listpairs, listone, listtwo):
    if listone[:3] == listtwo[-3:]:
        toadd = [carikey(dictdata, listtwo), carikey(dictdata, listone)]
        if toadd not in listpairs:
            listpairs.append(toadd)

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_grph.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs12.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)
dctdata = dict_fastaformat(seqs)
print(dctdata)

overlappairs = []
for listO3one in dctdata.values():
    for listO3two in dctdata.values():
        if listO3two != listO3one:
            overlapstring(dctdata, overlappairs, listO3one, listO3two)
            overlapstring(dctdata, overlappairs, listO3two, listO3one)

# print(pasangan)
print()
for i in range(len(overlappairs)):
    print(overlappairs[i][0], overlappairs[i][1])