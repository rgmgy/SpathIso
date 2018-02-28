# -*- coding:utf-8 -*-
#在这里实现查找pu在G中对应的路径ipu，要求是对于任意的pu中的p在ipu中有相应的路径。
#输入qp，candidate，PathG
#(vi,vi+1) (C(vi), C(vi+1))在pathg中
#找到一个instatiation就要去验证joinable，不通过的话，回溯找instatiation
#相当于用了两个递归，神经病

#对当前vi+1，找所有C(vi+1), 如果某个C(vi+1) 能够匹配，就加入(vi+1,C(vi+1))，令vi+1为当前点往前走，
# 如果所有不能，返回到vi,去掉当前匹配到的C(vi)，找新的C(vi)
#

def Instantiation(queryQ, candidateQ, NSG, cur_M, vertexsetG, all_M, i=1):


    v = queryQ[i]
    for cv in candidateQ[v]:
        mu = cur_M[queryQ[i - 1]]
        if cv not in NSG[mu][1][vertexsetG[mu]]:
            continue
        cur_M[v] = cv
        if i < len(queryQ-1):
            i += 1
            Instantiation(queryQ, candidateQ, NSG, cur_M, vertexsetG, i)
        else:
            all_M.append(cur_M)

            return all_M









