import os
DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data')
import snownlp as slp
import collections as clt
Comment=clt.namedtuple('Comment', 'content,result')
def get_contents(file_path):
    with open(file_path, 'r', encoding='utf8') as f:
        return [n.strip() for n in f.readlines()]
def analyse_to_comment(content):
    s=slp.SnowNLP(content)
    return Comment(display_long(content), pst_to_result(s.sentiments))
def display_long(content):
    if len(content)>10:
        return content[0:5] + '......' + content[-5:]
    return content
def pst_to_result(positive):
    if positive>0.75:
        return '好评'
    return '差评'
if __name__=="__main__":
    file=os.path.join(DATA_DIR, 'taobao.txt')
    print("")
    cms=(
        analyse_to_comment(c)
        for c in get_contents(file)
    )
    for c in cms:
        print(c)



