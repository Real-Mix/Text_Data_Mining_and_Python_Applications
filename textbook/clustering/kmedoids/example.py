# coding: utf-8
from sklearn.metrics.pairwise import pairwise_distances
#sklearn中可以直接通过计算余弦相似度得到相似度矩阵
import numpy as np
import kmedoids
# 文本集中的文档向量
data = np.array([[0.51,0.63,0.38], 
                [0.25,0.82,0.62], 
                [0.13,0.22,0.31]])
# 距离矩阵
D = pairwise_distances(data, metric='euclidean')
# 分成两组
M, C = kmedoids.kMedoids(D, 2)
print('')
print('medoids:')
for point_idx in M:
    print( data[point_idx] )
print('')
print('clustering result:')
for label in C:
    for point_idx in C[label]:
        print('label {0}:　{1}'.format(label, data[point_idx]))


