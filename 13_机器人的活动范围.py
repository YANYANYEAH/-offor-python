# -*- coding:utf-8 -*-
# // 面试题13：机器人的运动范围
# // 题目：地上有一个m行n列的方格。一个机器人从坐标(0, 0)的格子开始移动，它
# // 每一次可以向左、右、上、下移动一格，但不能进入行坐标和列坐标的数位之和
# // 大于k的格子。例如，当k为18时，机器人能够进入方格(35, 37)，因为3+5+3+7=18。
# // 但它不能进入方格(35, 38)，因为3+5+3+8=19。请问该机器人能够到达多少个格子？
import numpy as np


def get_sum(n):
    n_sum = 0
    while n != 0:
        n_sum += n%10
        n = n//10
    return n_sum


def get_path(a,m,n,i,j,k):
    if 0<=i<m and 0<=j<n and a[i,j] == 0 and get_sum(i) + get_sum(j) <= k:
        a[i,j] = 1
        get_path(a, m, n, i+1, j, k)
        get_path(a, m, n, i-1, j, k)
        get_path(a, m, n, i, j+1, k)
        get_path(a, m, n, i, j-1, k)


if __name__ == '__main__':
    m = input("请输入矩阵行数")
    n = input("请输入矩阵列数")
    k = input("请输入k值大小")
    a = np.zeros((m,n))
    get_path(a,m,n,0,0,k)
    print np.sum(a==1)