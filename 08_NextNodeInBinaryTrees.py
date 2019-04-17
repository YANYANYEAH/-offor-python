# -*- coding:utf-8 -*-

# 给中序，和一个节点，找下一个节点应该是什么
# // 面试题8：二叉树的下一个结点
# // 题目：给定一棵二叉树和其中的一个结点，如何找出中序遍历顺序的下一个结点？
# // 树中的结点除了有两个分别指向左右子结点的指针以外，还有一个指向父结点的指针。


class treeNode:
    def __init__(self,x=None):
        self.value = x
        self.left = None
        self.right = None
        self.parent = None


def connect_node(a, b, c):
    a.left = b
    a.right = c
    b.parent = a
    c.parent = a


def get_next(node):
    # next_node = treeNode()
    if node.right is not None:
        next_node = node.right
        while next_node.left is not None:
            next_node = next_node.left
        return next_node.value
    else:
        if node.parent.left == node:
            next_node = node.parent
            return next_node.value
        else:
            next_node = node
            while next_node.parent.right == next_node:
                next_node = next_node.parent
                if next_node.parent is None:
                    return None
            return next_node.parent.value



if __name__ == '__main__':
    a = treeNode("a")
    b = treeNode("b")
    c = treeNode("c")
    d = treeNode("d")
    e = treeNode("e")
    f = treeNode("f")
    g = treeNode("g")
    h = treeNode("h")
    i = treeNode("i")
    connect_node(a,b,c)
    connect_node(b,d,e)
    connect_node(e,h,i)
    connect_node(c,f,g)
    print get_next(d)
    print get_next(b)
    print get_next(h)
    print get_next(e)
    print get_next(i)
    print get_next(a)
    print get_next(f)
    print get_next(c)
    print get_next(g)


