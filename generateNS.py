# -*- coding:utf-8 -*-
import numpy as np

def N_Signature(k, VG, A, labelset):

    vertexNum = len(VG)

    result = [[{label: [] for label in labelset} for j in range(k)] for m in range(vertexNum)]
    C_result = [[{label: 0 for label in labelset} for j in range(k)] for m in range(vertexNum)]
    path = [[[] for i in range(vertexNum)] for j in range(vertexNum)]
    # 需要一个path[N][N]=[]记录每个点到其它点的路径，
    # result[vertexNum][k] = {'label': []}
    TA = A

    # T1 记录每个点自己的标签，T2记录到每个的最短距离为k的标签为l的点数量，T3记录到每个点的最短距离为k的标签为l的点的具体信息。
    for i in range(k):
        tempA = TA
        if i > 0:
            TA = TA.dot(A)

        TA = TA - np.diag(np.diag(TA))

        index = np.transpose(np.nonzero(TA))
        for j in index:
            label = VG[j[1]]
            flag = 0
            for m in range(i):

                if j[1] in result[j[0]][m][label]:
                    flag = 1
            if flag == 0:
                # 找tempA[j[0]]行中不为0的id，和A j[1]列中不为0的id，然后把path[j[0]][id]+id的值赋给path[j[0]][j[1]],这个id不唯一，所以
                # path[j[0]][j[1]] 暂时用多维数组，这样的话整个数组的形状不统一，path[j[0]][id]还可能有多条路径，每一条都要赋值。
                result[j[0]][i][label].append(j[1])
                C_result[j[0]][i][label] += 1
                '''
                path[i][j]记录了i到j的最短路径，最后搜索我实现的糙，没有用到这个信息。这一段还是有用的，等需要的时候，实现用path的搜索

                if i == 0:
                    t = [j[0], j[1]]
                    path[j[0]][j[1]].append(t)
                else:
                    index1 = np.nonzero(tempA[j[0]])[0]
                    index2 = np.nonzero(A[:, j[1]])[0]
                    same_id = np.where(np.in1d(index1, index2))[0]

                    for id in same_id:
                        tp = []
                        for p in path[j[0]][index1[id]]:

                            for tv in p:
                                tp.append(tv)
                            tp.append(j[1])
                            path[j[0]][j[1]].append(tp)
                '''

    return result, C_result
