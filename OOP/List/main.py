class Node:
    def __init__(self, prev, next_, value):
        self.prev = prev
        self.next = next_
        self.value = value


class List:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def append(self, value):
        new_node = Node(None, None, value)
        if self.head:
            new_node.next = None
            new_node.prev = self.tail

            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def __getitem__(self, i):  # []
        cur_i = 0
        node = self.head

        while True:
            if cur_i == i:
                return node.value
            else:
                node = node.next
                cur_i += 1

    def __str__(self):
        string = '['
        node = self.head
        while True:
            if node is None:
                break
            else:
                string += node.value.__repr__() + ", "
                node = node.next
        if string[-2:] == ', ':
            string = string[:-2]
        return string + ']'

    def __len__(self):  # len()
        node = self.head
        l = 0
        while True:
            if node is None:
                return l
            else:
                l += 1
                node = node.next


# n1 = Node(None, None, 'a')
# n2 = Node(None, None, 'b')
# n3 = Node(None, None, 'c')
#
# lst = List(n1, n3)
#
# n1.next = n2
# n2.next = n3
# n3.next = None
#
# n1.prev = None
# n2.prev = n1
# n3.prev = n2
#
# lst.append('d')
# lst.append('e')

#
# print(lst.head.next.next.next.next.value)
# print(lst.tail.value)


lst = List()
lst.append('a')
lst.append('b')
lst.append('c')


i = 0
while i < len(lst):
    print(lst[i])
    i += 1
