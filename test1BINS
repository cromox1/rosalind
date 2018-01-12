__author__ = 'cromox'

maksimum = 1 * 10**5

def input_binarysearch(filename):
    with open(filename) as f:
        n, m, nlists, mlists = [line.strip().split() for line in f.readlines()]
        mlist = [int(num) for num in mlists]  ### list comprehension
        nlist = [int(num) for num in nlists]
        m = [int(num) for num in m][0] # list(map(int, m))
        n = [int(num) for num in n][0] # list(map(int, n))
        return n, m, nlist, mlist

def compareandshrink(mval, nlist):
    nstrt = 0 ; nlast = len(nlist) - 1
    while nstrt <= nlast:
        nindex = int((nstrt + nlast)/2)
        # print('middle = ' + str(nindex))
        if nlist[nindex] > mval:
            nlast = nindex - 1
        elif nlist[nindex] < mval:
            nstrt = nindex + 1
        else:
            return nindex + 1  ## if found (same value), return index
    return -1  ## if not found, return -1

if __name__ == "__main__":
    filedirectory = r'C:\Users\cromox\Desktop\newselenium\rosalind\test2_binarysearch'
    # fileinput = r'\test_input1.txt'
    fileinput = r'\rosalind_bins.txt'
    filename = filedirectory + fileinput

    n = input_binarysearch(filename)[0]
    m = input_binarysearch(filename)[1]
    nlist = input_binarysearch(filename)[2]
    mlist = input_binarysearch(filename)[3]

    try:
        int(m) ; int(n)

        if n <= maksimum and m <= maksimum and m == len(mlist) and n == len(nlist) and n <= m:
            print('n = ' + str(n))
            print('m = ' + str(m))
            print('nlist = ' + str(nlist))
            print('mlist = ' + str(mlist))

            outputt = []
            for mval in mlist:
                index = compareandshrink(mval, nlist)
                outputt.append(index)

            ### OUTPUT
            for i in outputt:
                print(i,sep=' ',end=' ')
            print('')
            ## output in list format
            print('indices = ' + str(outputt))

        else:
            if n > maksimum:
                terlebih = n
            elif m > maksimum:
                terlebih = m
            print('value exceeded %s' %maksimum + ' , ie %s' %terlebih)
    except:
        print('problem with input file %s' %fileinput)
