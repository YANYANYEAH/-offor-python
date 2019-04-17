# -*- coding:utf-8 -*-

# // 面试题12：矩阵中的路径
# // 题目：请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有
# // 字符的路径。路径可以从矩阵中任意一格开始，每一步可以在矩阵中向左、右、
# // 上、下移动一格。如果一条路径经过了矩阵的某一格，那么该路径不能再次进入
# // 该格子。例如在下面的3×4的矩阵中包含一条字符串“bfce”的路径（路径中的字
# // 母用下划线标出）。但矩阵中不包含字符串“abfb”的路径，因为字符串的第一个
# // 字符b占据了矩阵中的第一行第二个格子之后，路径不能再次进入这个格子。
# // A B T G
# // C F C S
# // J D E H

import numpy as np
def haspath(a,str1,i,j,aa,pathlen):
    '''
        :param a:字符矩阵
        :param str1:需要寻找的路径
        :param i:当前位置的横坐标(对应列数)
        :param j:当前位置的纵坐标(对应行数)
        :param aa:访问标志数组
        :param pathlen:已经找到的路径长度
        :return:是否存在路径
    '''
    if pathlen == len(str1):
        return 1
    return_hasepath = 0
    # 参数校验：1、位置坐标不超过行列数 2、当前位置字符等于路径中对应位置的字符 3、当前位置未存在于当前已找到的路径中
    if 0 <= i < len(a) and 0 <= j < len(a[0]) and a[i][j] == str1[pathlen] and not aa[i][j]:
        aa[i][j] = 1
        pathlen += 1
        print i,j
        # 分别向左，向右，向上，向下移动一个格子，任一方向能够继续往下走均可
        return_hasepath = haspath(a,str1,i-1,j,aa,pathlen) or haspath(a,str1,i+1,j,aa,pathlen) \
                or haspath(a, str1, i, j-1, aa, pathlen) or haspath(a, str1, i, j+1, aa, pathlen)
        # 如果不能再走下一步，需要回退到上一状态
        if not return_hasepath:
            pathlen -= 1
            aa[i][j] = 0
    return return_hasepath


def get_path(a,str1):
    if len(str1) == 0 or len(a) == 0 or len(a[0])==0:
        return -1
    aa = np.zeros((len(a),len(a[0])))
    pathlen = 0
    for i in range(len(a)):
        for j in range(len(a[0])):
            if haspath(a,str1,i,j,aa,pathlen):
                return 1
            else:
                return 0


if __name__ == '__main__':
    a = [['a','b','t','g'],
         ['c','f','c','s'],
         ['j','d','e','h']]
    # str1 = "bfce"
    str1 = "abfb"
    print get_path(a, str1)