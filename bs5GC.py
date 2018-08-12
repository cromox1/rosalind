__author__ = 'cromox'

def inputfile(filename):
    with open(filename) as f:
        xx = f.read().replace('\n','').split('>')
        f.close()
    return xx

#pathfile = r'C:\Users\cromox\Downloads\\'
#fileinput = 'rosalind_gc.txt'
pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
fileinput = 'input_bs5.txt'
filename = pathfile + fileinput

seqs = inputfile(filename)
# print(seqs)

dctdata = {}
for seq in seqs:
    if len(seq) > 0:
        print(seq)
        key = seq[:13]
        value = seq[13:]
        dctdata[key] = value

#print('dctdata # = ' + str(dctdata))

percentage = dict({(k,(v.count('G')+v.count('C'))*100/len(v)) for k,v in dctdata.items()})
print(percentage)

print()
for k,v in percentage.items():
    if v == max(percentage.values()):
        print(k + '\n' + str(v))

