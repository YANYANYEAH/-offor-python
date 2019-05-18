# -*- coding:utf-8 -*-
# // 面试题18（二）：删除链表中重复的结点
# // 题目：在一个排序的链表中，如何删除重复的结点？例如，在图3.4（a）中重复
# // 结点被删除之后，链表如图3.4（b）所示。

class creat_node:
    def __init__(self, x):
        self.value = x
        self.next = None


def connect(x,y):
    x.next = y


def delete_double(head):
    if head.next is None or head.next.next is None:
        return
    p1 = head
    p2 = p1.next      # 注意：此处为临界条件，为了防止删掉后前一个节点指针的next，所以要记录前一个指针
    val = 0
    while p2.next:
        if p2.next.value == p2.value or p2.value == val:  # 注意：当存在相等值的时候val便会赋值
            val = p2.value
            temp = p2
            p2 = p2.next
            p1.next = p2
            del temp
        else:
            p1 = p2
            p2 = p2.next
    if p2.value == val:  # 因为上一个临界条件是p2存在next，所以当p2为最后一个节点的时候就不再进入判断
        p1.next = None
        del p2


def print_list(head):
    temp = head          # 注意 打印从temp.next开始，此时就不用进行最后一步的判断
    while temp.next:
        print temp.next.value
        temp = temp.next


if __name__ == '__main__':
    head = creat_node(0)
    a = creat_node(1)
    b = creat_node(2)
    c = creat_node(3)
    d = creat_node(3)
    e = creat_node(4)
    f = creat_node(4)
    g = creat_node(5)
    connect(head, a)
    connect(a, b)
    connect(b, c)
    connect(c, d)
    connect(d, e)
    connect(e, f)
    connect(f, g)
    delete_double(head)
    print_list(head)
