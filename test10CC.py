__author__ = 'cromox'

# http://rosalind.info/problems/cc/
#
# My algorithm works on the example and some my own simple test cases, but fails on the actual problem (downloaded dataset)
# Need to investigate WHY !!!!
#

def filetolist(filename):
    with open(filename) as f:
        matrixlist = [line.strip().split() for line in f.readlines()]
        f.close()
        netcount1 = len(matrixlist[1:])
        nodecount = int(matrixlist[0][0])
        netcount2 = int(matrixlist[0][1])
    return matrixlist, netcount1, nodecount, netcount2

def datatonettlist(matrixlist):
    mlist = []
    sortdmlist = []
    for inlist in matrixlist[1:]:
        kk = int(inlist[0])
        vv = int(inlist[1])
        mlist.append([kk,vv])
        sortdmlist.extend([kk,vv])
    sortdmlist.sort()
    uniqlist = list(set(sortdmlist))
    return mlist, uniqlist

def putintogroup(int1, int2, grouplist, grpno):
    if int1 in grouplist[grpno] or int2 in grouplist[grpno]:
        if int1 not in grouplist[grpno]:
            grouplist[grpno].append(int1)
        if int2 not in grouplist[grpno]:
            grouplist[grpno].append(int2)
        stop = 1
    else:
        stop = 0
    return grouplist, grpno, stop

if __name__ == "__main__":
    filedirectory = r'C:\Users\cromox\Desktop\newselenium\rosalind\test10_connectd_components'
    # fileinput = r'\test_input1.txt'
    # fileinput = r'\rosalind_cc.txt'
    fileinput = r'\test_input2.txt'
    filename = filedirectory + fileinput

    listone = filetolist(filename)[0]
    jaringan = filetolist(filename)[3]
    nodesemua = filetolist(filename)[2]

    mlist = datatonettlist(listone)[0]
    numlist = len(mlist)
    uniqnetx = datatonettlist(listone)[1]

    print('mlist = ' + str(mlist))
    print('len mlist = ' + str(len(mlist)))
    print('uniqnetx = ' + str(uniqnetx))
    print('len uniqnetx = ' + str(len(uniqnetx)))

    kump = []
    kump.append(mlist[0])
    maxkump = int(len(mlist))
    for i in range(uniqnetx[0], maxkump):
        kump.append([])
    #print('kump = ' + str(kump))
    #print('len kump = ' + str(len(kump)))

    for j in range(1,numlist):
        for grp in range(0, len(kump)):
            masukgroup = putintogroup(mlist[j][0], mlist[j][1], kump, grp)
            kump = masukgroup[0]
            grp = masukgroup[1]
            henti = masukgroup[2]
            # print('kump now = ' + str(kump) + ' / int1,int2 = ' + str(mlist[j][0]) + ',' + str(mlist[j][1]) + ' / grp = ' + str(grp))
            if henti == 1:
                break
        if grp == (numlist - 1):
            newgrp = len([x for x in kump if x != []])
            kump[newgrp].extend([mlist[j][0], mlist[j][1]])

    kumpnewone = [x for x in kump if x != []]

    print('')
    print('kumpnewone = ' + str(kumpnewone))
    print('len kumpnewone = ' + str(len(kumpnewone)))
    print('')
    print('numnodeall = ' + str(nodesemua))
    numnodeuse = len(uniqnetx)
    print('numnodeuse = ' + str(numnodeuse))
    answer = len(kumpnewone) + (nodesemua - numnodeuse)
    print('')
    print('ANSWER = ' + str(answer))
