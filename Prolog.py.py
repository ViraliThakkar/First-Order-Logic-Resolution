from copy import deepcopy
import time
flagf = False
def unify (str):
    ffll = []
    for vv in range(len(str)):
        stt = ''
        c1 = 0
        flag2 = True
        i1 = str[vv].find('(')
        q = str[vv][0:i1]
        if i1 >= 1 and q[0] == '~':
            q1 = q[1:]
        else:
            q1 = '~' + q

        for j1 in range(len(kb)):#str1
            stemp = ''.join(kb[j1])
            fl = 1

            for j11 in range(len(kb[j1])):
                l1 = kb[j1][j11].find('(')
                s1 = kb[j1][j11][0:l1]
                ffl = []
                if s1 == q1:
                    c1 = c1 + 1
                    #print(kb[j1][j11])
                    i11 = str[vv].find(')')
                    qq = str[vv][i1+1:i11]
                    t1 = qq.rstrip().split(',')
                    l11 = kb[j1][j11].find(')')
                    ss = kb[j1][j11][l1+1:l11]
                    t2 = ss.rstrip().split(',')

                    for j2 in range(len(t1)):
                        ss1 = ''.join(t1[j2])
                        ss2 = ''.join(t2[j2])
                        if t1[j2][0].islower() and t2[j2][0].islower():
                            fl = 0
                            if j2 == 0:
                                stt = stemp.replace(t2[j2],t1[j2])
                            else:
                                stt = stt.replace(t2[j2], t1[j2])
                        elif t1[j2][0].isupper() and t2[j2][0].islower():
                            fl = 0
                            if j2 == 0:
                                stt = stemp.replace(t2[j2],t1[j2])
                            else:
                                stt = stt.replace(t2[j2], t1[j2])
                        elif t1[j2][0].islower() and t2[j2][0].isupper():
                            fl = 0
                            if j2 == 0:
                                stt = stemp.replace(t1[j2],t2[j2])
                            else:
                                stt = stt.replace(t1[j2],t2[j2])
                        elif t1[j2][0].isupper() and t2[j2][0].isupper():
                            if t1[j2] != t2[j2]:
                                fl = 1
                    if fl == 0:
                        cnt = 0
                        #ffl = []
                        '''for jj in range(len(finalq)):
                            for jj1 in range(len(finalq[jj])):
                                if finalq[jj][jj1] == str:
                                    del finalq[jj]'''
                        ff = stt.rstrip('\n').split(')')
                        for j3 in range(len(ff)-1):
                            j4 = ff[j3].find('(')
                            if ff[j3][j4+1].isupper():
                                cnt += 1
                            ss3 = ff[j3] + ')'
                            if str[vv][0] == '~':
                                q11 = str[vv][1:]
                            else:
                                q11 = '~' + str[vv]
                            if q11 != ss3:
                                ffl.append(ss3)
            if ffl and c1 == 1:
                flag2 = True
                for idx4 in range(len(gen)):
                    if ffl == gen[idx4]:
                        flag2 = False
                if flag2 == True:
                    '''finalq.append(ffl)
                    gen.append(ffl)'''
                    ffll.append(ffl)
                    #break
                #if ffl:
                 #   break
            elif ffl:
                flag2 = True
                for idx4 in range(len(gen)):
                    if ffl == gen[idx4]:
                        flag2 = False
                for idx4 in range(len(ffll)):
                    lt = []
                    lt.append(ffll[idx4])
                    if lt[0].append(ffl) == ffll[idx4]:
                        flag2 = False
                    if flag2 == True:
                        ffll[idx4].append(ffl)
    for vv1 in range(len(ffll)):
        finalq.append(ffll[vv1])
        gen.append(ffll[vv1])

    if final == finalq and len(final) == 1:
        print('False')
    flag1 = False
    for jj in range(len(finalq)):
        #for jj1 in range(len(finalq[jj])):
        if finalq[jj] == str:
            del finalq[jj]
            flag1 = True
            '''if not finalq[jj]:
                del finalq[jj]'''
            break
        if flag1 == True:
            break
        #finalq = [[]]
    '''if flag1 == True and flag2 == True:
        flagf = True
    else:
        flagf = False'''
    '''if cnt == len(ff)-1:
        finalkb.append(ffl)
    else:
        kbc.append(ffl)'''
    print(finalq)
list = []
qlist = []
kb = []
kbc = []
finalkb = []
finalq = []
gen = []
flag1 = False
flag2 = True
fo = open('input.txt','r')
i = 0
with open('input.txt') as f:
    for line in f:
        if i==0:
            j = int(line)
        elif i <= j:
            tl = line.rstrip('\n').split('|')
            qlist.append(tl)
        elif i>=j+2:
            tl = line.rstrip('\n').split('|')
            list.append(tl)
        i+=1
fo.close()

flag = True
for idx in range(len(qlist)):
    flag = True
    final = []
    st = []
    st.append(qlist[idx][0])
    st1 = st
    if st[0][0] == '~':
        st[0] = st[0][1:]
    else:
        st[0] = '~' + st[0]
    final.append(st)
    gen.append(st)
    kb = []
    finalkb = []
    for idx1 in range(len(list)):
        if len(list[idx1])==1:
            if st == list[idx1][0]:
                print('False')
            if st1 == list[idx1][0]:
                print('True')
            i1 = list[idx1][0].find('(')
            i2 = list[idx1][0].find(')')
            v = list[idx1][0][i1+1:i2]
            v1 = v.split(',')
            f = 0
            for i in range(len(v1)-1):
                if v1[i].islower():
                    f = 1
            if f == 0:
                finalkb.append(list[idx1][0])
        else:
            kb.append(list[idx1])
        #print(kb)

    while flag == True:
        if not final and flag1 == True and flag2 == True:
            print('True')
        flag = False
        kbc = deepcopy(kb)
        #time.sleep(2)
        #print(kb)
        finalq = deepcopy(final)
        for idx1 in range(len(final)):
            for idx2 in range(len(final[idx1])):
                for idx22 in range(len(finalkb)):
                    if finalkb[idx22] == final[idx1][idx2]:
                        flag == True
                        del final[idx1][idx2]
                        if not final[idx1]:
                            print('True')
                            final = [[]]
                        break
                if flag == False:
                    #for idx3 in range(len(kb)):
                    unify(final[idx1])
                    if final == finalq:
                        print('False')
                    else:
                        final = finalq
                        flag = True
                    for idx3 in range(len(final)):
                        if not final[idx3] and flag1 == True and flag2 == True:
                            print('True')
                if not final and flag1 == True and flag2 == True:
                    print('True')
                    break
                if flag == True:
                    break
            if flag == True:
                break


