"""coding=utf-8
8.2  Закодируйте любую строку по алгоритму Хаффмана.
"""

from collections import Counter
from operator import itemgetter


class MyNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'{self.value = }\n -> {self.left = } {self.right = }'


counter_ = Counter("beep boop beer!")
print(counter_)
ordered_struct = sorted(counter_.items(), key=itemgetter(1))
ind = 0
while True:
    if len(ordered_struct) == 1:
        break
    weight = ordered_struct[ind][1] + ordered_struct[ind + 1][1]
    print(f' {weight = }')
    node = MyNode("node")
    node.left = MyNode(ordered_struct[ind][0])
    node.right = MyNode(ordered_struct[ind + 1][0])
    print(f'step 1:{ordered_struct}')
    # удаляем эти элементы
    ordered_struct.pop(ind)
    ordered_struct.pop(ind)
    print(f'step 2:{ordered_struct}')
    # вставка элемента
    for j, item in enumerate(ordered_struct):
        # print(j, item, item[1], item[1] >= weight)
        if item[1] >= weight:
            break
        if j == len(ordered_struct) - 1:
            j += 1
    #     print(f' индекс вставки:{j}')
    ordered_struct.insert(j, (node, weight))
    print(f'step 3:{ordered_struct}')
    print(f' индекс вставки {j = }')
