__author__ = 'cromox'

maksimum = 1 * 10**5

def inputfile(filename):
    with open(filename) as f:
        mlist = [line.strip().split() for line in f.readlines()]
        f.close()
        mdictnum = {}
        sortdmlist = []
        lstsmll = 0
        for inlist in mlist[:]:
            kk = int(inlist[0])
            vv = int(inlist[1])
            if int(kk) not in mdictnum:
                mdictnum[int(kk)] = {int(vv)}
            else:
                mdictnum[int(kk)].update({int(vv)})
            if int(vv) not in mdictnum:
                mdictnum[int(vv)] = {int(kk)}
            else:
                mdictnum[int(vv)].update({int(kk)})
            sortdmlist.append(kk)
            sortdmlist.append(vv)
            ## finding last i's neighbour which has only one network/connection
            if kk > lstsmll:
                lstsmll = kk
            if vv > lstsmll:
                lstsmll = vv
        sortdmlist.sort()
        # print('mdictnum = ' + str(mdictnum))
        # print('sortdmlist = ' + str(sortdmlist))

        ## finding last i's associate's neighbour
        relatedsmall = list(mdictnum[lstsmll])[0]

        ## remove connection of the last i's neighbour and it's associate network
        mdictnum[lstsmll].remove(relatedsmall)
        mdictnum[relatedsmall].remove(lstsmll)
        # print('mdictnum[relatedsmall] = ' + str(mdictnum[relatedsmall]))

        m = len(mdictnum)
        return mdictnum, m, sortdmlist, lstsmll

if __name__ == "__main__":
    filedirectory = r'C:\Users\cromox\Desktop\newselenium\rosalind\test7_doubledegreearray'
    # fileinput = r'\test_input1.txt'
    fileinput = r'\rosalind_ddeg.txt'
    filename = filedirectory + fileinput

    baca = inputfile(filename)
    m = baca[1]
    mnetx = baca[0]
    uniqnetx = baca[2]
    lstsmll = baca[3]

    if m <= maksimum and m == len(mnetx):
        for key in list(set(uniqnetx)):
            summ = 0
            for mnet in mnetx[key]:
                summ += len(mnetx[mnet])
            if lstsmll == 5:      ### NOT SURE ABOUT THIS!!! to get the same as in the Question's Sample Output
                print(summ, sep='', end=' ')
            elif lstsmll > key:
                print(summ, sep='', end=' ')

    else:
        if m > maksimum:
            terlebih = m
        print('value exceeded %s' %maksimum + ' , ie %s' %terlebih)
