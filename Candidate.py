# -*- coding:utf-8 -*-
#找q中的所有点v在g中的candidate，
#v的candidate u 需要和v有相同的label，
#input：VG，VQ


def candidate(VQ, VG):
    num_VQ = len(VQ)
    result = [[] for i in range(num_VQ)]

    #在字典中for时取的是字典的key，v是VQ的key，
    for v in VQ:
        for u in VG:

            if VQ[v] == VG[u]:
                #如果两者的label相同，将u加入到v的candidate列表
                result[v].append(u)
    return result
