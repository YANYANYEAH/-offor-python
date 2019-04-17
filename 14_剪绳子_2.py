# -*- coding:utf-8 -*-
# // 面试题14：剪绳子
# // 题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m≥1）。
# // 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘
# // 积是多少？例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此
# // 时得到最大的乘积18。

# 使用贪婪算法，思想很难，基本放弃


def get_max(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    m = n/3
    if n%3 == 1:
        return 4*(3**(m-1))
    elif n%3 == 2:
        return 3**m *2
    else:
        return 3**m


if __name__ == '__main__':
    n = input("请输入n：")
    print get_max(n)
