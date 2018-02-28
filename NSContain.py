# -*- coding:utf-8 -*-

#CNSQ[vertexnum][k][label] = int
#sub_count 记录距离u，v最短距离为k的标签为l的点的数量差
#在这里调用candidate进一步处理

sub_count = []
def Contain(Cnsq, Cnsg, vq, vg, labelsetq):
    K = len(Cnsq[0])
    #num_label = len(Cnsq[0][0])
    for i in range(K):
        for j in labelsetq:
            if Cnsq[vq][i][j] > Cnsg[vg][i][j]:
                return False
            sub_count.append(Cnsg[vg][i][j]-Cnsq[vq][i][j])
    return True