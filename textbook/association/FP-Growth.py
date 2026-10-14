import pprint
def loadDataSet():
    dataSet = [['文本','数据','挖掘','模式','资料','分析'],
          ['数据','分析'],
          ['文本','存储','分析'],
          ['文本','查找','分析'],
          ['文本','挖掘','存储']]
    return dataSet
def transfer2FrozenDataSet(dataSet):
    frozenDataSet = {}
    for elem in dataSet:
        frozenDataSet[frozenset(elem)] = 1
    return frozenDataSet
class TreeNode:
    def __init__(self, nodeName, count, nodeParent):
        self.nodeName = nodeName
        self.count = count
        self.nodeParent = nodeParent
        self.nextSimilarItem = None
        self.children = {}
    def increaseC(self, count):
        self.count += count
def createFPTree(frozenDataSet, minSupport):
    #第一次扫描数据集，筛选出小于支持的项
    headPointTable = {}
    for items in frozenDataSet:
        for item in items:
            headPointTable[item] = headPointTable.get(item, 0) + frozenDataSet[items]
    headPointTable = {
        k: v
        for k, v in headPointTable.items() if v >= minSupport
    }
    frequentItems = set(headPointTable.keys())
    if len(frequentItems) == 0: return None, None
    for k in headPointTable:
        headPointTable[k] = [headPointTable[k], None]
    fptree = TreeNode("null", 1, None)
    #第二次扫描数据集，筛选出每个记录的项
    for items, count in frozenDataSet.items():
        frequentItemsInRecord = {}
        for item in items:
            if item in frequentItems:
                frequentItemsInRecord[item] = headPointTable [item][0]
        if len(frequentItemsInRecord) > 0:
            frequentItemsInRecord = sorted(frequentItemsInRecord. items(), key=lambda v: v[0])
            orderedFrequentItems = [v[0] for v in sorted(frequentItemsInRecord,key=lambda v:v[1], reverse=True)]
            updateFPTree(fptree, orderedFrequentItems, headPointTable, count)
    return fptree, headPointTable
def updateFPTree(fptree, orderedFrequentItems, headPointTable, count):
    #处理第一项
    if orderedFrequentItems[0] in fptree.children:
        fptree.children[orderedFrequentItems[0]].increaseC(count)
    else:
        fptree.children[orderedFrequentItems[0]] = TreeNode(orderedFrequentItems[0], count, fptree)
         # 修改头结点表
        if headPointTable[orderedFrequentItems[0]][1] == None:
            headPointTable[orderedFrequentItems[0]][1] = fptree.children[orderedFrequentItems[0]]
        else:            updateHeadPointTable(headPointTable[orderedFrequentItems[0]][1], fptree.children[orderedFrequentItems[0]])
    # 处理除第一项外的其他项
    if (len(orderedFrequentItems) > 1):
        updateFPTree(fptree.children[orderedFrequentItems[0]], orderedFrequentItems[1::], headPointTable, count)
def updateHeadPointTable(headPointBeginNode, targetNode):
    while (headPointBeginNode.nextSimilarItem != None):
        headPointBeginNode = headPointBeginNode.nextSimilarItem
    headPointBeginNode.nextSimilarItem = targetNode
def mineFPTree(headPointTable, prefix, frequentPatterns, minSupport):
    #对于头结点表的每一项, 查找条件前缀路径，创建条件FP树
    #然后迭代，直到条件FP树中只有一个元素
    headPointItems = [v[0] for v in sorted(headPointTable.items(), key=lambda v: v[1][0])]
    if (len(headPointItems) == 0): return
    for headPointItem in headPointItems:
        newPrefix = prefix.copy()
        newPrefix.add(headPointItem)
        support = headPointTable[headPointItem][0]
        frequentPatterns[frozenset(newPrefix)] = support
        prefixPath = getPrefixPath(headPointTable, headPointItem)
        if (prefixPath != {}):
            conditionalFPtree, conditionalHeadPointTable = createFPTree(prefixPath, minSupport)
            if conditionalHeadPointTable != None:
                mineFPTree(conditionalHeadPointTable, newPrefix, frequentPatterns, minSupport)
def getPrefixPath(headPointTable, headPointItem):
    prefixPath = {}
    beginNode = headPointTable[headPointItem][1]
    prefixs = ascendTree(beginNode)
    if ((prefixs != [])):
        prefixPath[frozenset(prefixs)] = beginNode.count
    while (beginNode.nextSimilarItem != None):
        beginNode = beginNode.nextSimilarItem
        prefixs = ascendTree(beginNode)
        if (prefixs != []):
            prefixPath[frozenset(prefixs)] = beginNode.count
    return prefixPath
def ascendTree(treeNode):
    prefixs = []
    while ((treeNode.nodeParent!=None) and (treeNode.nodeParent. nodeName != 'null')):
        treeNode = treeNode.nodeParent
        prefixs.append(treeNode.nodeName)
    return prefixs
def rulesGenerator(frequentPatterns, minConf, rules):
    for frequentset in frequentPatterns:
        if (len(frequentset) > 1):
            getRules(frequentset, frequentset, rules, frequentPatterns,minConf)
def removeStr(set, str):
    tempSet = []
    for elem in set:
        if (elem != str):
            tempSet.append(elem)
    tempFrozenSet = frozenset(tempSet)
    return tempFrozenSet
def getRules(frequentset, currentset, rules, frequentPatterns, minConf):
    for frequentElem in currentset:
        subSet = removeStr(currentset, frequentElem)
        confidence = frequentPatterns[frequentset] / frequentPatterns[subSet]
        if (confidence >= minConf):
            flag = False
            for rule in rules:
                if (rule[0] == subSet and rule[1] == frequentset - subSet):
                    flag = True
            if (flag == False):
                rules.append((subSet, frequentset - subSet, confidence))
            if (len(subSet) >= 2):
                getRules(frequentset, subSet, rules, frequentPatterns, minConf)
if __name__ == '__main__':
    dataSet = loadDataSet()
    frozenDataSet = transfer2FrozenDataSet(dataSet)
    minSupport = 3
    fptree, headPointTable = createFPTree(frozenDataSet, minSupport)
    frequentPatterns = {}
    prefix = set([])
    mineFPTree(headPointTable, prefix, frequentPatterns, minSupport)
    print("")
    print("frequent patterns:")
    pprint.pprint(frequentPatterns)
    minConf = 0.6
    rules = []
    rulesGenerator(frequentPatterns, minConf, rules)
    print("association rules:")
    pprint.pprint(rules)
    print('rules num:', len(rules))
