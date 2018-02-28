# -*- coding:utf-8 -*-
#输入Candidate, CNSQ, CNSG, PathQ
#对每个v的所有candidate u 首先找到最小的kmin使得 sum(CNSG[u][k][l])-sum(CNSQ[v][k][l])>0, 对任意的l,开始应该是等于0，然后某个k开始大于0
#然后选出PathQ 中长度小于mink的path，由QueryPath[QVnum]={u:[[路径]]} 记录。

def path_candidate(VQ, Cnsq, Cnsg, Pathq, candidate, k, labelsetq):

    result = [[] for i in range(len(VQ))]
    for v in VQ:
        for u in candidate[v]:
            mink = 0
            a = {u:[]}
            for i in range(k):
                subCNS = 0
                for l in labelsetq:
                    subCNS += Cnsg[u][i][l] - Cnsq[v][i][l]
                if subCNS > 0:
                    mink = i + 1

            if mink > 0:
                for j in range(len(VQ)):
                    for path in Pathq[v][j]:
                        if len(path)-1 < mink or len(path)-1 == mink:
                            a[u].append(path)
                result[v].append(a)
            else:
                #当v基于u找不到两者都是最短距离的path时，直接对点进行查询
                a[u].append([v])
                result[v].append(a)
    return result


