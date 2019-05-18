# -*- coding:utf-8 -*-
# // 面试题14：剪绳子
# // 题目：给你一根长度为n绳子，请把绳子剪成m段（m、n都是整数，n>1并且m≥1）。
# // 每段的绳子的长度记为k[0]、k[1]、……、k[m]。k[0]*k[1]*…*k[m]可能的最大乘
# // 积是多少？例如当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此
# // 时得到最大的乘积18。

# 使用动态规划的方法 ， 其中n为输入值，m只要>1就可以，不是一个固定值.


def get_max(n):
    max_list = [0,1,2,3]
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        for j in range(4, n+1):
            max_n = 0
            for i in range(1, j):
                temp = max_list[i]*max_list[j-i]
                if temp > max_n:
                    max_n = temp
            max_list.append(max_n)
        return max_list[n]


if __name__ == '__main__':
    n = input("请输入n：")
    print get_max(n)