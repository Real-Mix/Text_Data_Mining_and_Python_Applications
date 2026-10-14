import random

'''
    python解决三门问题

    @author sage zsj

    三门问题（Monty Hall problem）亦称为蒙提霍尔问题、蒙特霍问题或蒙提霍尔悖论，
    大致出自美国的电视游戏节目Let's Make a Deal。问题名字来自该节目的主持人
    蒙提·霍尔（Monty Hall）。参赛者会看见三扇关闭了的门，其中一扇的后面有一辆汽车，
    选中后面有车的那扇门可赢得该汽车，另外两扇门后面则各藏有一只山羊。
    当参赛者选定了一扇门，但未去开启它的时候，节目主持人开启剩下两扇门的其中一扇，露出其中一只山羊。
    主持人其后会问参赛者要不要换另一扇仍然关上的门。问题是：换另一扇门会否增加参赛者赢得汽车的机率？
'''


class Door:
    contain = 'sheep'

    def __repr__(self):
        return 'There is a ' + self.contain + ' behind this door'


def three_door_problem(reselect, redo=100):
    right = 0
    for _ in range(redo):
        # 放置三道门，里面都是羊
        three_door = [Door(), Door(), Door()]
        # 随机将一道门后的羊换成车
        random.choice(three_door).contain = 'car'
        # 随便猜一道门
        choose_door = random.choice(three_door)
        # 打开另外两道门中含有羊的一道门
        rother_door = [door for door in three_door if not door is choose_door]
        for door in rother_door:
            if door.contain == 'sheep':
                rother_door.remove(door)
                break
        # 去掉错误答案后，是否重新选择另外一门
        if reselect == True:
            choose_door = rother_door.pop()
        # 统计选中车的次数
        if choose_door.contain == 'car':
            right += 1
    print('进行了{0}次三门问题，是否重选 = {1}，选中车概率为{2:.2%}'.format(
        redo, reselect, right/redo))


three_door_problem(False, 10000)
three_door_problem(True, 10000)
