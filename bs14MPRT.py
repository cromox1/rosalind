__author__ = 'cromox'

'''
( http://rosalind.info/problems/mprt/ )

Problem

To allow for the presence of its varying forms, a protein motif is represented by a shorthand as follows: [XY] means
"either X or Y" and {X} means "any amino acid except X." For example, the N-glycosylation motif is written as
N{P}[ST]{P}.
You can see the complete description and features of a particular protein by its access ID "uniprot_id" in the UniProt
database, by inserting the ID number into
http://www.uniprot.org/uniprot/uniprot_id
http://www.uniprot.org/uniprot/uniprot_id.fasta

Given: At most 15 UniProt Protein Database access IDs.
Return: For each protein possessing the N-glycosylation motif, output its given access ID followed by a list of
locations in the protein string where the motif can be found.
'''
from urllib.request import urlretrieve as getuniprotfasta
def inputfile(filename):
    with open(filename) as f:
        xx = f.read().replace('\n','##').split('##')
        f.close()
        xxx = [x for x in xx if len(x) > 0]
    return xxx

def trans_1unifasta(onefastalist):
    name = onefastalist[0]
    fastalist = [x for x in onefastalist[1:] if len(x) > 0]
    # fasta = ''.join(map(str, fastalist))
    seqfasta = ''.join(fastalist)
    return name, seqfasta

pathfile = r'C:\Users\cromox\Downloads\\'
fileinput = 'rosalind_mprt.txt'
#pathfile = r'C:\Users\cromox\Desktop\newselenium\rosalind\\'
#fileinput = 'input_bs14.txt'
filename = pathfile + fileinput

uniprot_ids = inputfile(filename)
print(uniprot_ids)
print()
for prot_id in uniprot_ids:
    urluniprot = 'https://www.uniprot.org/uniprot/' + prot_id +'.fasta'
    getuniprotfasta(urluniprot, prot_id + '.fasta')
    fastalist = inputfile(prot_id + '.fasta')
    nameandseqs = trans_1unifasta(fastalist)
    seqs = nameandseqs[1]
    try:
        import os
        os.remove(prot_id + '.fasta')
    except:
        pass
    toprint = []
    for i in range(len(seqs)-3):
        if seqs[i] == 'N' and seqs[i+1] != 'P' and seqs[i+2] == 'S' and seqs[i+3] != 'P':
            toprint.append(i+1)
        elif seqs[i] == 'N' and seqs[i+1] != 'P' and seqs[i+2] == 'T' and seqs[i+3] != 'P':
            toprint.append(i+1)
    if len(toprint) > 0:
        print(prot_id)
        print(*toprint)
