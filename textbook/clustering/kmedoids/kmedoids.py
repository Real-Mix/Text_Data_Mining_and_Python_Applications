import numpy as np
import random
def kMedoids(D, k, tmax=100):
    # 确定矩阵D的维数
    m, n = D.shape
    if k > n:
        raise Exception('too many medoids')
    # 随机初始化k-medoid一组指标
    M = np.arange(n)
    np.random.shuffle(M)
    M = np.sort(M[:k])
    # 创建medoid指标副本
    Mnew = np.copy(M)
    # 初始化
    C = {}
    for t in range(tmax):
        # 确定簇
        J = np.argmin(D[:,M], axis=1)
        for kappa in range(k):
            C[kappa] = np.where(J==kappa)[0]
        # 修改聚类
        for kappa in range(k):
            J = np.mean(D[np.ix_(C[kappa],C[kappa])],axis=1)
            j = np.argmin(J)
            Mnew[kappa] = C[kappa][j]
        np.sort(Mnew)
        # 检查类别
        if np.array_equal(M, Mnew):
            break
        M = np.copy(Mnew)
    else:
        # 对聚类成员进行更新
        J = np.argmin(D[:,M], axis=1)
        for kappa in range(k):
            C[kappa] = np.where(J==kappa)[0]
    # 返回结果
    return M, C
