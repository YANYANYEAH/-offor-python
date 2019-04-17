# -*- coding:utf-8 -*-
# // 面试题9：用两个栈实现队列
# // 题目：用两个栈实现一个队列。队列的声明如下，请实现它的两个函数appendTail
# // 和deleteHead，分别完成在队列尾部插入结点和在队列头部删除结点的功能。

# 编程 python list
# list.pop(int) 根据索引删除，参数必须为int型
# list.remove(' ') 根据元素删除，参数不做要求，删除符合要求的第一个元素

# tips:
# 在实现栈、队列时，每次操作都需要修改指针的位置！！


class Stack:
    def __init__(self):
        self.top = 0
        self.stack = []

    def puch(self,a):
        self.stack.append(a)
        self.top += 1

    def pop(self):
        if self.top == 0:
            return None
        else:
            return_num = self.stack[self.top-1]
            self.stack.pop(self.top-1)
            self.top -= 1
            return return_num

class Queue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def appendTail(self, a):
        self.stack1.puch(a)

    def deleteHead(self):
        if self.stack2.top == 0:
            while self.stack1.top != 0:
                temp = self.stack1.pop()
                self.stack2.puch(temp)
            return self.stack2.pop()
        else:
            return self.stack2.pop()

if __name__ == '__main__':
    queue = Queue()
    queue.appendTail('a')
    queue.appendTail('b')
    queue.appendTail('c')
    print queue.deleteHead()
    print queue.deleteHead()
    queue.appendTail('d')
    print queue.deleteHead()
    queue.appendTail('e')
    print queue.deleteHead()
    print queue.deleteHead()
    # print queue.deleteHead()
