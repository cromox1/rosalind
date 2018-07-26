__author__ = 'cromox'

maksimum = 1 * 10**5

def inputfile(filename):
    with open(filename) as f:
        m1, m1lists, m2, m2lists = [line.strip().split() for line in f.readlines()]
        f.close()
        m1list = [int(num) for num in m1lists]  ### list comprehension
        m1 = [int(num) for num in m1][0] # list(map(int, m))
        m2list = [int(num) for num in m2lists]  ### list comprehension
        m2 = [int(num) for num in m2][0] # list(map(int, m))
        return m1, m1list, m2, m2list

def insertionsort(mlist):
    istart = 1
    istop = len(mlist) - 1
    swaps = 0

    for i in range(istart, istop + 1):
        for k in range(istop, i - 1, -1):
            totukar = mlist[k]
            ditukar = mlist[k - 1]
            if totukar < ditukar :
                mlist[k], mlist[k - 1] = ditukar, totukar  ## fastest way to SWAP
                swaps = swaps + 1
                # print('swaps = ' + str(swaps) + ' / k = %s ' %k + ' / totukar = ' + str(totukar) + ' / ditukar = ' + str(ditukar))
    return mlist, swaps

if __name__ == "__main__":
    filedirectory = r'C:\Users\cromox\Desktop\newselenium\rosalind\test5_merge_sorted'
    # fileinput = r'\test_input1.txt'
    fileinput = r'\rosalind_mer2.txt'
    filename = filedirectory + fileinput

    inputnyer = inputfile(filename)

    m1 = inputnyer[0]
    m2 = inputnyer[2]
    m1list = inputnyer[1]
    m2list = inputnyer[3]

    try:
        int(m1)
        int(m2)

        if m1 <= maksimum and m1 == len(m1list) and m2 <= maksimum and m2 == len(m2list):
            print('m1 = ' + str(m1))
            print('m1list = ' + str(m1list))
            print('m2 = ' + str(m2))
            print('m2list = ' + str(m2list))

            mlist = []
            for list in [m1list, m2list]:
                for val in list:
                    mlist.append(val)

            print('mlist = ' + str(mlist))

            msorted = insertionsort(mlist)

            # print('msorted = ' + str(msorted[0]))

            print('')
            for val in msorted[0]:
                print(val, sep=' ', end=' ')
            print('')

        else:
            if m1 > maksimum:
                terlebih = m1
            elif m2 > maksimum:
                terlebih = m2
            print('value exceeded %s' %maksimum + ' , ie %s' %terlebih)
    except:
        print('problem with input file %s' %fileinput)
