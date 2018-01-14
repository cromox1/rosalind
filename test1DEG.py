__author__ = 'cromox'

maksimum = 1 * 10**5

def inputfile(filename):
    with open(filename) as f:
        du = []
        mlist = [line.strip().split() for line in f.readlines()]
        f.close()
        print('mlist = ' + str(mlist))
        for inlist in mlist[1:]:
            if int(inlist[0]) > int(inlist[1]):
                inlist[0],inlist[1] = inlist[1],inlist[0]
            # print('inlist ' + str(inlist))
            du.append(int(inlist[0]))
            du.append(int(inlist[1]))
            du.sort()

        m = len(du)
        return du, m

if __name__ == "__main__":
    filedirectory = r'C:\Users\cromox\Desktop\newselenium\rosalind\test4_degreearray'
    # fileinput = r'\test_input1.txt'
    fileinput = r'\rosalind_deg.txt'
    filename = filedirectory + fileinput

    baca = inputfile(filename)
    m = baca[1]
    mlist = baca[0]

    try:
        int(m)

        if m <= maksimum and m == len(mlist):
            print('m = ' + str(m))
            print('mlist = ' + str(mlist))

            for val in list(set(mlist)):
                print(mlist.count(val), sep=' ', end=' ')

        else:
            if m > maksimum:
                terlebih = m
            print('value exceeded %s' %maksimum + ' , ie %s' %terlebih)
    except:
        print('problem with input file %s' %fileinput)
