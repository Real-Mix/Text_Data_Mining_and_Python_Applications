import os
import jieba
f_path=os.path.join(os.path.dirname(os.path.abspath(__file__)), '1.txt')
with open(f_path) as f:
   contents=f.read()
   seg_list = jieba.cut(contents,cut_all=False)
   print('/'.join(seg_list))


