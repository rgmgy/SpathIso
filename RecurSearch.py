# -*- coding:utf-8 -*-
#输入candidate，一个Q，一个G，要在G中找到Q,f，NSQ,NSG,labset
#DFS，当前匹配节点v，搜索所有v的candidate，
# 如果有一个能够match，就从v的一步邻居中挑一个，作为下一个检查的需要匹配的节点，递归
#如果v的candidate都不能match，返回到上一个匹配好的节点，从它的还没有检查过的candidate挑选出新的可以匹配的
#如果一路回到了第一个匹配的节点还是找不到，就说明没有Q的embedding
#如果一路到了最后一个节点依然能够匹配，就返回这个匹配的路径。
#初始的match cur_M = [[v,c(v)]], all_M = []

#改三个地方：
# 1、当匹配到一个完整的Q时，当前的v不能返回，还要继续检查当前v的其它candidate
# 2、查找下一个节点的方法

########
#递归：想不清楚的时候，实际走一遍，大概两步就够了。
# 注意参数，停止条件，返回值
#

import numpy as np

def recurMatch(v, Q, G, nsq, nsg, candidate, labset, cur_M, all_M):
    for cv in candidate[v]:
        flag = 0
        #判断当前的v的cv是否和之前所有已经匹配的G中节点有边
        if len(cur_M) != 0:
            for match in cur_M:
                if v in nsq[match[0]][0][Q[v]]:
                    tem_M = np.array(cur_M)
                    if (cv not in nsg[match[1]][0][G[cv]]) or (cv in tem_M[:, 1]):

                        flag = 1
        #在这一层，[v,cv]是可以匹配的
        if flag == 0:
            cur_M.append([v, cv])
            if len(cur_M) == len(Q):
                #不能直接all_M.appedn(cur_M),不然回溯的时候all_M会随着cur_M改变
                tall_M = []
                for i in range(len(cur_M)):
                    tall_M.append(cur_M[i])

                all_M.append(tall_M)
            else:
                # 挑选下一个进行匹配的节点，这里实现得比较糙，直接选了当前节点的一个一步邻居（label随意）
                # 后面这里可以优化一下，没准可以减少搜索的步骤
                # 这里我用了当前匹配节点的一步邻居作为下一个节点，但是可能一步邻居已经匹配，且没有其它的邻居，也就出现了Q3这种图没办法匹配的问题
                # 要用随机的没有匹配的节点。

                tem_M2 = np.array(cur_M)
                u = -1
                i = 0
                while u == -1 and i < len(Q):
                    if i not in tem_M2[:, 0]:
                        u = i
                    else:
                        i += 1

                all_M = recurMatch(u, Q, G, nsq, nsg, candidate, labset, cur_M, all_M)




            cur_M.pop()
    return all_M



