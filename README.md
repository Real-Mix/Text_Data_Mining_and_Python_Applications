# Text_Data_Mining_and_Python_Applications

《文本数据挖掘与Python应用》（作者：刘金岭、钱升华；出版社：清华大学出版社）课本配套的代码整理，希望能帮到需要的同学。

![image](https://github.com/Real-Mix/HUZHOU_TextualAnalysis/assets/98143224/1e46e2ee-f5f7-42d7-af49-274a2512bff1)

内容包括：

1. 词云图的构建（非书本要求，见 `wordcloud/`）；
2. 原书网站上的部分现成代码及部分习题代码（见 `textbook/`）；
3. 书中阴影部分的全部代码（见 `notebooks/`）。

## 目录结构

```
.
├── README.md
├── requirements.txt
├── notebooks/                    # 文本数据挖掘与python应用final.ipynb：书中代码汇总 Notebook
├── textbook/                     # 教材源代码和部分习题源代码
│   ├── classification/           # 分类：朴素贝叶斯（例4-3）、决策树 ID3 / C4.5、treePlotter 绘图
│   ├── clustering/               # 聚类：kmedoids、鸢尾花数据聚类、Pycluster 安装包（Windows .exe）
│   ├── association/              # 关联规则：Apriori、FP-Growth
│   ├── sentiment/                # 情感分析：senti_python（例7-1）、商品评论（SnowNLP）
│   ├── keywords-summary/         # 关键词与摘要：提取关键词、TextRank4ZH 实验、生成摘要、文本相似度、wordCloudCount
│   ├── misc/                     # 其他：三门问题、pomegranate 建模、example01、ch2-ex4（正向/逆向最大匹配）
│   ├── exercises/                # 习题：ex2-5
│   └── data/                     # 共享数据：语料、情感词典（positive/negative/否定词/程度级别词语）、停用词、sales.db 等
└── wordcloud/                    # 词云项目（源自 fuqiuai/wordCloud）
    ├── demo.py / chnSegment.py / plotWordcloud.py
    ├── doc/  Images/  font/  userdict/
```

脚本中的数据路径已改为相对于脚本自身位置（`os.path.dirname(__file__)`），原先的 `D://python3sy/` 等绝对路径不再需要。

## 环境与安装

建议 Python 3.8 及以上：

```bash
pip install -r requirements.txt
```

`textbook/clustering/Pycluster-1.59.win-amd64-py3.6/` 为原书提供的 Windows 安装包（仅适用于 Python 3.6 / 64 位 Windows）。

## 运行方法

在任意目录下直接运行脚本即可，例如：

```bash
python textbook/sentiment/商品评论.py
python textbook/association/Apriori.py
python "textbook/classification/决策树分类（C4-5）.py"
python wordcloud/demo.py
```

Notebook：`jupyter notebook notebooks/`。

注意：
- `textbook/keywords-summary/wordCloudCount.py` 使用 Windows 字体 `C:/Windows/Fonts/simhei.ttf`，其他系统请自行修改字体路径（可用 `wordcloud/font/msyh.ttf`）。
- TextRank4ZH 相关脚本依赖的 `networkx` 新版本移除了 `from_numpy_matrix`，如报错可安装 `networkx<3`。
- 部分数据文件为 GBK 编码（原书在 Windows 下编写）。

## 致谢 / 引用

- `wordcloud/` 目录源自开源项目 [fuqiuai/wordCloud](https://github.com/fuqiuai/wordCloud)，版权归原作者所有。
- 教材代码来自《文本数据挖掘与Python应用》（刘金岭、钱升华，清华大学出版社）。

## 声明

本仓库代码仅供学习交流使用，请勿用于商业用途。
