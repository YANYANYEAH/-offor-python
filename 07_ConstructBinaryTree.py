# -*- coding:utf-8 -*-

# 树只需要创建节点类，不需要创建树类

# 知道前序和中序，给树结构
# 使用递归的方法。
class TreeNode:
    def __init__(self, x=None):
        self.value = x
        self.left = None
        self.right = None


def build_tree(pre_array, tin_array):
    if len(pre_array) == 0:
        return None
    else:
        root = TreeNode(pre_array[0])
        num = tin_array.index(pre_array[0])
        root.left = build_tree(pre_array[1:num+1], tin_array[:num])
        root.right = build_tree(pre_array[num+1:],tin_array[num+1:])
        return root


if __name__ == '__main__':
    pre_array = [1,2,4,7,3,5,6,8]
    tin_array = [4,7,2,1,5,3,8,6]
    tree = build_tree(pre_array,tin_array)