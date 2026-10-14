from numpy import *
#朴素贝叶斯算法
"""--------------------------------------------------------------
函数1：创建实验样本。
功能说明：将文本切分成词条。
返回值说明：trainData是词条，labels则是词条对应的分类标签。
-----------------------------------------------------------------
"""
def loadDataSet():
    trainData=[['我的', '狗', '有', '跳蚤', '问题', '帮助', '请'], 
       ['可能', '不会', '使得', '它的', '到', '狗', '公园', '愚蠢'],
       ['我的', '斑点狗', '是', '也', '机灵', '我', '喜欢', '它'],
       ['停止', '张贴', '愚蠢', '毫无价值', '垃圾'],
       ['先生', '舔', '吃', '我的', '牛排', '怎么做', '到', '停下', '它'],
       ['退出', '购买', '毫无价值', '狗', '食物', '愚蠢']]
    labels=[0, 1, 0, 1, 0, 1] #1表示侮辱性言论，0表示正常言论
    return trainData, labels
#生成词汇表
    return postingList,classVec   #返回实验样本切分的词条和类别标签向量
"""--------------------------------------------------------------
函数2: 制作词汇表。
函数说明：将切分的实验样本词条整理成不重复的词条列表，也就是词汇表。
参数说明：dataSet是上面的trainData，也就是重复的词条样本集，而vocabList则是无重复的词汇表。
-----------------------------------------------------------------
"""
def createVocabList(trainData):
    VocabList = set([])
    for item in trainData:
        VocabList = VocabList|set(item) #取两个集合的并集
    return sorted(list(VocabList))    #对结果排序后返回
"""--------------------------------------------------------------
函数3：词汇向量化。
函数说明: 根据vocabList词汇表（也就是上面函数制作的词汇表），将trainData（输入的词汇）向量化，向量的每个元素为1或0，如果词汇表中有这个单词就置1，没有就置0。
参数说明：最后返回的是文档向量。
功能：对训练数据生成只包含0和1的向量集。
-----------------------------------------------------------------
"""
def createWordSet(VocabList, trainData):
    VocabList_len = len(VocabList)   #词汇集的长度
    trainData_len = len(trainData)   #训练数据的长度
    WordSet = zeros((trainData_len,VocabList_len))     #生成行长度为训练数据的长度 列长度为词汇集的长度的列表
    for index in range(0,trainData_len):
        for word in trainData[index]:
            if word in VocabList:     #其实也就是，训练数据包含的单词对应的位置为1其他为0
                WordSet[index][VocabList.index(word)] = 1
    return WordSet
"""--------------------------------------------------------------
函数4：朴素贝叶斯分类器训练函数。
函数说明: 利用朴素贝叶斯求出分类概率，也可以说是求出先验概率。
参数说明：输入参数WordSet是所有样本数据矩阵，每行是一个样本，一列代表一个词条。
输入参数labels是所有样本对应的分类标签，是一个向量，维数等于矩阵的行数。
输出参数p0是一个向量，维数与上面相同，每个元素表示对应样本的概率。
输出参数p1是一个向量，和上面那个向量互补（因为是二分类问题），每个元素对应样本的概率。
-----------------------------------------------------------------
"""
def opreationProbability(WordSet, labels):
       WordSet_col = len(WordSet[0])
       #每条样本中的词条数量
       labels_len = len(labels)
       #训练集中样本数量
       WordSet_labels_0 = zeros(WordSet_col)
       WordSet_labels_1 = zeros(WordSet_col)
       num_labels_0 = 0
       num_labels_1 = 0
       for index in range(0,labels_len):
           if labels[index] == 0:
               WordSet_labels_0 += WordSet[index]   
               num_labels_0 += 1
               #统计正常言论的条件概率所需的数据，即P(w0|0),P(w1|0),P(w2|0)••• 
           else:
               WordSet_labels_1 += WordSet[index] 
               num_labels_1 += 1
               #统计侮辱性言论的条件概率所需的数据，即P(w0|1),P(w1|1),P(w2|1)•••
       p0 = WordSet_labels_0 * num_labels_0 / labels_len
       p1 = WordSet_labels_1 * num_labels_1 / labels_len
       return p0, p1
      #返回侮辱性言论的条件概率数组，正常言论的条件概率数组
"""--------------------------------------------------------------
#主程序调用
-----------------------------------------------------------------
"""
trainData, labels = loadDataSet()
VocabList = createVocabList(trainData)
train_WordSet = createWordSet(VocabList,trainData)
p0, p1 = opreationProbability(train_WordSet, labels)
#到此就算是训练完成
#开始测试
print()
testData1= [['喜欢', '我的', '斑点狗']]     #测试样本1
print("测试样本1['喜欢', '我的', '斑点狗']：",end="")
test_WordSet = createWordSet(VocabList, testData1)  #测试数据的向量集
res_test_0 = sum(p0 * test_WordSet)
res_test_1 = sum(p1 * test_WordSet)

if res_test_0 > res_test_1:
    print("属于0类别，即为正常言论。")
else:
    print("属于1类别，即为侮辱性言论。")
testData2= ['愚蠢', '垃圾']   #测试样本2
print("测试样本2['愚蠢', '垃圾']：",end="")
test_WordSet = createWordSet(VocabList, testData2)  #测试数据的向量集
res_test_0 = sum(p0 * test_WordSet)
res_test_1 = sum(p1 * test_WordSet)
if res_test_0 > res_test_1:
    print("属于0类别，即为正常言论。")
else:
    print("属于1类别，即为侮辱性言论。")

