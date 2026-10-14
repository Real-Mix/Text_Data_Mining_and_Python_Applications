from numpy import *
def loadDataSet():
   # return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]
   return[['文本','数据','挖掘','模式','资料','分析'],
          ['数据','分析'],
          ['文本','存储','分析'],
          ['文本','查找','分析'],
          ['文本','挖掘','存储']]
# 获取候选1项集，dataSet为事务集。返回一个list，每个元素都是set集合
def createC1(dataSet):
    C1 = []   # 元素个数为1的项集（非频繁项集，因为还没有同最小支持度比较）
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()  
    return list(map(frozenset, C1))   
# 找出候选集中的频繁项集
# dataSet为全部数据集，Ck为大小为k（包含k个元素）的候选项集，minSupport为设定的最小支持度
def scanD(dataSet, Ck, minSupport):
    ssCnt = {}   # 记录每个候选项的个数
    for tid in dataSet:
        for can in Ck:
            if can.issubset(tid):
                ssCnt[can] = ssCnt.get(can, 0) + 1   
# 计算每一个项集出现的频率
    numItems = float(len(dataSet))
    retList = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key] / numItems
        if support >= minSupport:
            retList.insert(0, key)  #将频繁项集插入返回列表的首部
        supportData[key] = support
    return retList, supportData  
 #retList为在Ck中找出的频繁项集（支持度大于minSupport的），supportData记录各频繁项集的支持度
# 通过频繁项集列表Lk和项集个数k生成候选项集C(k+1)。
def aprioriGen(Lk, k):
    retList = []
    lenLk = len(Lk)
    for i in range(lenLk):
        for j in range(i + 1, lenLk):
            # 前k-1项相同时，才将两个集合合并，合并后才能生成k+1项
            L1 = list(Lk[i])[:k-2]; L2 = list(Lk[j])[:k-2]   
# 取出两个集合的前k-1个元素
            L1.sort(); L2.sort()
            if L1 == L2:
                retList.append(Lk[i] | Lk[j])
    return retList
# 获取事务集中的所有的频繁项集
def apriori(dataSet, minSupport=0.5):
    C1 = createC1(dataSet)  # 从事务集中获取候选1项集
    D = list(map(set, dataSet))  # 将事务集的每个元素转化为集合
    L1, supportData = scanD(D, C1, minSupport)  
# 获取频繁1项集和对应的支持度
    L = [L1]  # L用来存储所有的频繁项集
    k = 2
    while (len(L[k-2]) > 0): 
# 一直迭代到项集数目过大而在事务集中不存在这种n项集
        Ck = aprioriGen(L[k-2], k)   
# 根据频繁项集生成新的候选项集。Ck表示项数为k的候选项集
        Lk, supK = scanD(D, Ck, minSupport)  
# Lk表示项数为k的频繁项集，supK为其支持度
        L.append(Lk);supportData.update(supK)  
# 添加新频繁项集和他们的支持度
        k += 1
    return L, supportData
if __name__=='__main__':
    dataSet = loadDataSet()  # 获取事务集。每个元素都是列表
    L, suppData = apriori(dataSet,minSupport=0.7)
    print("")
    print(L,suppData)
