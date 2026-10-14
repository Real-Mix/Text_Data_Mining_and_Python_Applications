import random
#坚持选择模拟10000次
prize = ['山羊','山羊','汽车']
count = 0
for i in range(10000):
    random.shuffle(prize)
    if prize[random.randint(0,2)] == 'car':
        count += 1
print('坚持选择的概率:%.6f' %(count/10000))
#改变选择，模拟10000次
count = 0
for i in range(10000):
    prize = ['山羊','山羊','汽车']
    random.shuffle(prize)
    choice = random.randint(0,2)
    prize.pop(choice)
    prize.remove('山羊')
    if prize[0] == '汽车':
        count += 1
print('更改选择的概率:%6f' %(count/10000))
