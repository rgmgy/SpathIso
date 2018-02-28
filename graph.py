# -*- coding:utf-8 -*-
import numpy as np

class GraphSet:
    def __init__(self, inputFile):
        self.__graphSet = []
        self.__vertexSet = []
        self.__edgeSet = []
        self.__VlableSet = []
        self.__ElableSet = []
        try:
            with open(inputFile, "r") as fin:
                lineNum = -1
                curVertexSet = {}
                curEdgeSet = {}
                curVlabelset = []
                curElabelset = []

                for line in fin:
                    lineList = line.strip().split(" ")
                    if not lineList:
                        print "Class GraphSet __init__() line split error!"
                        exit()
                    # a new graph!
                    if lineList[0] == 't':
                        # write it to graphSet
                        if lineNum > -1:
                            currentGraph = (lineNum, curVertexSet, curEdgeSet)
                            self.__graphSet.append(currentGraph)
                            self.__vertexSet.append(curVertexSet)
                            self.__edgeSet.append(curEdgeSet)
                            self.__VlableSet.append(curVlabelset)
                            self.__ElableSet.append(curElabelset)
                            # print "Class GraphSet __init__  __graphSet: ", self.__graphSet
                            # print "Class GraphSet __init__  __vertexSet: ", self.__vertexSet
                            # print "Class GraphSet __init__  __edgeSet: ", self.__edgeSet
                        lineNum += 1
                        curVertexSet = {}
                        curEdgeSet = {}
                    elif lineList[0] == 'v':
                        if len(lineList) != 3:
                            print "Class GraphSet __init__() line vertex error!"
                            exit()
                        curVertexSet[int(lineList[1])] = lineList[2]
                        if lineList[2] not in curVlabelset:
                            curVlabelset.append(lineList[2])

                    elif lineList[0] == 'e':
                        if len(lineList) != 4:
                            print "Class GraphSet __init__() line edge error!"
                            exit()
                        edgeKey = str(lineList[1]) + ":" + str(lineList[2])
                        curEdgeSet[edgeKey] = lineList[3]
                        if lineList[3] not in curElabelset:
                            curElabelset.append(lineList[3])
                    else:
                        # empty line!
                        continue
        except IOError, e:
            print "Class GraphSet __init__() Cannot open Graph file: ", e
            exit()

    def graphSet(self):
        return self.__graphSet

    def curVSet(self, offset):
        if offset >= len(self.__vertexSet):
            print "Class GraphSet curVSet() offset out of index!"
            exit()

        return self.__vertexSet[offset]

    def curESet(self, offset):
        if offset >= len(self.__edgeSet):
            print "Class GraphSet curESet() offset out of index!"
            exit()

        return self.__edgeSet[offset]

    def curLabelSet(self, offset):
        if offset >= len(self.__vertexSet):
            print "Class GraphSet curLabelSet() offset out of index!"
            exit()

        return self.__VlableSet[offset]

    def curVESet(self, offset):

        if offset >= len(self.__vertexSet):
            print "Class GraphSet curVESet() offset out of index!"
            exit()

        vertexNum = len(self.__vertexSet[offset])
        result = [[] for i in range(vertexNum)]

        for key in self.__edgeSet[offset]:
            v1, v2 = key.strip().split(":")
            # print int(v1)
            # print int(v2)
            result[int(v1)].append(key)
            result[int(v2)].append(key)
        return result

    def neighbor(self, offset, vertexIndex):
        if offset >= len(self.__vertexSet):
            print "Class GraphSet neighbor() offset out of index!"
            exit()

        VESet = self.curVESet(offset)
        aList = VESet[vertexIndex]
        neighborSet = []
        for i in range(len(aList)):
            v1, v2 = aList[i].strip().split(":")
            if int(v1) != vertexIndex:
                neighborSet.append(int(v1))
            elif int(v2) != vertexIndex:
                neighborSet.append(int(v2))
            else:
                exit()
        return neighborSet

    def Adjmatrix(self, offset):
        if offset >= len(self.__vertexSet):
            print "Class GraphSet neighbor() offset out of index!"
            exit()
        vertexNum = len(self.__vertexSet[offset])
        result = np.zeros([vertexNum, vertexNum])

        for key in self.__edgeSet[offset]:
            v1, v2 = key.strip().split(":")
            # print int(v1)
            # print int(v2)
            result[int(v1)][int(v2)] = 1
            result[int(v2)][int(v1)] = 1
        return result

    '''
    def N_Signature(self, offset, k, A):
        if offset >= len(self.__vertexSet):
            print "Class GraphSet neighbor() offset out of index!"
            exit()
        vertexNum = len(self.__vertexSet[offset])
        VLNum = len(self.__VlableSet[offset])
        ELNum = len(self.__ElableSet[offset])

        result = [[{label:[] for label in self.__VlableSet[offset]} for j in range(k)] for m in range(vertexNum)]
        C_result = [[{label:0 for label in self.__VlableSet[offset]} for j in range(k)] for m in range(vertexNum)]
        path = [[[] for i in range(vertexNum)] for j in range(vertexNum)]
        #需要一个path[N][N]=[]记录每个点到其它点的路径，
        #result[vertexNum][k] = {'label': []}
        TA = A

        #T1 记录每个点自己的标签，T2记录到每个的最短距离为k的标签为l的点数量，T3记录到每个点的最短距离为k的标签为l的点的具体信息。
        for i in range(k):
            tempA = TA
            if i > 0:
                TA = TA.dot(A)

            TA = TA - np.diag(np.diag(TA))

            index = np.transpose(np.nonzero(TA))
            for j in index:
                label = self.__vertexSet[offset][j[1]]
                flag = 0
                for m in range(i):

                    if j[1] in result[j[0]][m][label]:
                        flag = 1
                if flag == 0:
                    #找tempA[j[0]]行中不为0的id，和A j[1]列中不为0的id，然后把path[j[0]][id]+id的值赋给path[j[0]][j[1]],这个id不唯一，所以
                    #path[j[0]][j[1]] 暂时用多维数组，这样的话整个数组的形状不统一，path[j[0]][id]还可能有多条路径，每一条都要赋值。
                    result[j[0]][i][label].append(j[1])
                    C_result[j[0]][i][label] += 1

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





        return result, C_result
    '''










