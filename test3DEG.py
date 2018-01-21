__author__ = 'cromox'

maksimum = 1 * 10**5

def inputfile(filename):
    with open(filename) as f:
        hubungan = {}
        mlist = [line.strip().split() for line in f.readlines()]
        f.close()
        print('mlist = ' + str(mlist))
        for inlist in mlist[1:]:
            if int(inlist[0]) not in hubungan:
                hubungan[int(inlist[0])] = 1
            else:
                hubungan[int(inlist[0])] +=1
            if int(inlist[1]) not in hubungan:
                hubungan[int(inlist[1])] = 1
            else:
                hubungan[int(inlist[1])] +=1

        m = len(hubungan)
        return hubungan, m

if __name__ == "__main__":
    filedirectory = r'C:\Users\cromox\Desktop\newselenium\rosalind\test4_degreearray'
    fileinput = r'\test_input1.txt'
    # fileinput = r'\rosalind_deg.txt'
    filename = filedirectory + fileinput

    baca = inputfile(filename)
    m = baca[1]
    mnetx = baca[0]

    if m <= maksimum and m == len(mnetx):
        print('m = ' + str(m))
        print('mnetx = ' + str(mnetx))

        sortedmnetx = sorted(mnetx.items())
        for k, v in sortedmnetx:
            print(v, sep='', end=' ')

    else:
        if m > maksimum:
            terlebih = m
        print('value exceeded %s' %maksimum + ' , ie %s' %terlebih)
