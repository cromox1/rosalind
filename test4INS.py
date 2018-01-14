__author__ = 'cromox'

maksimum = 1 * 10**5

def inputfile(filename):
    with open(filename) as f:
        m, mlists = [line.strip().split() for line in f.readlines()]
        f.close()
        mlist = [int(num) for num in mlists]  ### list comprehension
        m = [int(num) for num in m][0] # list(map(int, m))
        return m, mlist

### https://www.toptal.com/developers/sorting-algorithms/insertion-sort
## ALGORITHM:
#
#for i = 2:n,
#    for (k = i; k > 1 and a[k] < a[k-1]; k--)
#        swap a[k,k-1]
#
#    → invariant: a[1..i] is sorted
#end

def insertionsort2(mlist):
    istart = 1
    istop = len(mlist) - 1
    swaps = 0

    for i in range(istart, istop + 1):
        tukar = mlist[i]
        lastone = i - 1
        while (lastone >= 0) and (tukar < mlist[lastone]):
            mlist[lastone + 1] = mlist[lastone]
            lastone = lastone - 1
            swaps = swaps + 1
            print('swaps = ' + str(swaps) + ' mlist = ' + str(mlist[lastone]) + ' tukar = ' + str(tukar))
        mlist[lastone + 1] = tukar
    return mlist, swaps

def insertionsort(mlist):
    istart = 1
    istop = len(mlist) - 1
    swaps = 0

    for i in range(istart, istop + 1):
        for k in range(istop, i - 1, -1):
            tukar = mlist[k]
            dtukar = mlist[k - 1]
            if tukar < dtukar :
                mlist[k], mlist[k - 1] = dtukar, tukar  ## fastest way to SWAP
                swaps = swaps + 1
                print('swaps = ' + str(swaps) + ' / k = %s ' %k + ' / tukar = ' + str(tukar) + ' / dtukar = ' + str(dtukar))

    return mlist, swaps

if __name__ == "__main__":
    filedirectory = r'C:\Users\cromox\Desktop\newselenium\rosalind\test3_insertionsort'
    fileinput = r'\test_input1.txt'
    # fileinput = r'\rosalind_ins.txt'
    filename = filedirectory + fileinput

    m = inputfile(filename)[0]
    mlist = inputfile(filename)[1]

    try:
        int(m)

        if m <= maksimum and m == len(mlist):
            print('m = ' + str(m))
            print('mlist = ' + str(mlist))
            print('swap = ' + str(insertionsort(mlist)[1]))
            print('mlist = ' + str(insertionsort(mlist)[0]))


        else:
            if m > maksimum:
                terlebih = m
            print('value exceeded %s' %maksimum + ' , ie %s' %terlebih)
    except:
        print('problem with input file %s' %fileinput)
