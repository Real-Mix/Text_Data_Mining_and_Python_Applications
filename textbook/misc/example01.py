#-*- encoding:utf-8 -*-
from __future__ import print_function
import os
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass
import codecs
from textrank4zh import TextRank4Keyword, TextRank4Sentence
text = codecs.open(os.path.join(DATA_DIR, '002.txt'), 'r', 'utf-8').read()
tr4w = TextRank4Keyword()

tr4w.analyze(text=text, lower=True, window=2)   # py2中text必须是utf8编码的str或者unicode对象，py3中必须是utf8编码的bytes或者str对象
tr4s = TextRank4Sentence()
tr4s.analyze(text=text, lower=True, source = 'all_filters')
print()
print( '摘要：' )
for item in tr4s.get_key_sentences(num=3):
    print(item.sentence)
    #print(item.index, item.weight, item.sentence)
