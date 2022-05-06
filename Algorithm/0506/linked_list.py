class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        init = Node('init')
        self.head = init
        self.tail = init

        self.현재노드 = None
        self.데이터수 = 0

    def __len__(self):
        return self.데이터수

    def __str__(self):
        현재노드 = self.head
        현재노드 = 현재노드.next
        s = ''
        for i in range(self.데이터수):
            s += f'{현재노드.data}, '
            현재노드 = 현재노드.next
        return f'[{s[:-2]}]'

    def __iter__(self):
        현재노드 = self.head
        현재노드 = 현재노드.next
        while 현재노드:
            yield 현재노드.data
            현재노드 = 현재노드.next

    def append(self, data):
        새로운노드 = Node(data)
        self.tail.next = 새로운노드
        self.tail = 새로운노드
        self.데이터수 += 1

    def insert(self, input_index, input_data):
        현재노드 = self.head

        for i in range(input_index):
            현재노드 = 현재노드.next

        신규노드 = Node(input_data)
        신규노드.next = 현재노드.next
        현재노드.next = 신규노드
        self.데이터수 += 1

    def pop(self):
        마지막값 = self.tail.data
        현재노드 = self.head

        for i in range(self.데이터수):
            if 현재노드.next is self.tail:
                self.tail = 현재노드
                break
            현재노드 = 현재노드.next
        self.데이터수 -= 1
        return 마지막값

    def find(self, data):
        index = -1
        현재노드 = self.head
        for i in range(self.데이터수 + 1):
            if 현재노드.data == data:
                return index
            현재노드 = 현재노드.next
            index += 1
        return -1

# 새로운 인스턴스
L = LinkedList()
# append 수행
L.append(10)
L.append(20)
L.append(30)
L.append(40)
L.append(50)
L.append(15)

print(L)                        # str 함수 작성하기 전 : <__main__.LinkedList object at 0x10b420bb0>
print(L.head.data)              # init
print(L.head.next.data)         # 10
print(L.head.next.next.data)    # 20
print(L.tail.data)              # 15
print(L.데이터수)                 # 6

print('----------------------------------------')

# 매직메서드로 len 함수 구현
print(len(L))                   # 6
print(L)                        # str 함수 작성한 후 : [10, 20, 30, 40, 50, 15]

print('----------------------------------------')

print(L.pop())                  # 15
print(L)                        # [10, 20, 30, 40, 50]

print('----------------------------------------')

print(L.find(20))               # 1
print(L.find(5))                # -1

print('----------------------------------------')

for i in L:
    print(i)

"""
10
20
30
40
50
15
"""

print('----------------------------------------')

L.insert(2, 10000)
print(L)                # [10, 20, 10000, 30, 40, 50]

L.insert(3, 1000000)
print(L)                # [10, 20, 10000, 1000000, 30, 40, 50]