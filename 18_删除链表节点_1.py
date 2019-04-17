# -*- coding:utf-8 -*-
# // 面试题18（一）：在O(1)时间删除链表结点
# // 题目：给定单向链表的头指针和一个结点指针，定义一个函数在O(1)时间删除该
# // 结点。


class list_node:
    def __init__(self, x):
        self.value = x
        self.next = None

    def __del__(self):
        return


def connect_node(a,b):
    a.next = b


def deletd_node(x):
    if x.next == None:
        temp = head
        while temp.next != x:
            temp = temp.next
        temp.next = None           # 注意：当被删除的为最有一个节点的时候，前一个节点next和value都要更改，不要忘了改value
        if head.next == None:
            return -1
        else:
            del x
    else:
        x.value = x.next.value
        temp = x.next
        x.next = x.next.next
        del temp


def print_list(head):
    temp = head       # 注意 打印从temp.next开始，此时就不用进行最后一步的判断
    while temp.next:
        print temp.next.value
        temp = temp.next


if __name__ == '__main__':
    head = list_node(0)
    a = list_node(1)
    b = list_node(2)
    c = list_node(3)
    d = list_node(4)
    connect_node(head,a)
    connect_node(a,b)
    connect_node(b,c)
    connect_node(c,d)
    if deletd_node(a) != -1:
        print_list(head)
    else:
        print None