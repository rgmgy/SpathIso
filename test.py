# -*- coding:utf-8 -*-
from graph import GraphSet
from Candidate import candidate
from NSContain import Contain
from PathChick import path_candidate
from Next_Insstantiation import Instantiation
from RecurSearch import recurMatch
from generateNS import N_Signature

input_fileq = '/Users/gy/PycharmProjects/SpathIso/Data/Q2'
input_fileg = '/Users/gy/PycharmProjects/SpathIso/Data/G3'

Q = GraphSet(input_fileq)
G = GraphSet(input_fileg)

offset = 0

A_Q, A_G = Q.Adjmatrix(offset), G.Adjmatrix(offset)

NSQ, NS_CQ = N_Signature(3, Q.curVSet(offset), A_Q, Q.curLabelSet(offset))
NSG, NS_CG = N_Signature(3, G.curVSet(offset), A_G, G.curLabelSet(offset))

CandidatesInG = candidate(Q.curVSet(offset), G.curVSet(offset))
#print CandidatesInG

VQ_num = len(Q.curVSet(offset))

CandidatesInG_final = [[] for i in range(VQ_num)]

minid = 0
for i in range(VQ_num):
    for j in CandidatesInG[i]:
        if Contain(NS_CQ, NS_CG, i, j, Q.curLabelSet(offset)):
            CandidatesInG_final[i].append(j)
    if len(CandidatesInG_final[i]) < len(CandidatesInG_final[minid]):
        minid = i

#query_path = path_candidate(Q.curVSet(offset), NS_CQ, NS_CG, PathQ, CandidatesInG_final, 2, Q.curLabelSet(offset))

#teq = [0,1,3]

#match = Instantiation(teq, candidateQ=CandidatesInG_final, NSG=NSG, cur_M=[5], vertexsetG=G.curVSet(offset), all_M=[], i=1)

v = minid
curM = []
allM = []

#Q, G, nsq, nsg, candidate, labset, cur_M, all_M
match_list = recurMatch(v, Q.curVSet(offset), G.curVSet(offset), NSQ, NSG, CandidatesInG_final, Q.curLabelSet(offset), curM, allM )
for match in match_list:
    print match



print '...'

