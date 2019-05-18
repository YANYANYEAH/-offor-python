# -*- coding:utf-8 -*-
# // 面试题17：打印1到最大的n位数
# // 题目：输入数字n，按顺序打印出从1最大的n位十进制数。比如输入3，则
# // 打印出1、2、3一直到最大的3位数即999。

# # 最笨的方法，可能会出现大数问题
# def get_value(n):
#     if n <= 0:
#         return -1
#     else:
#         result = []
#         max_data = 10 ** n
#         for i in range(max_data):
#             result.append(i)
#         return result


# 使用递归的思想
import copy
def get_value(n):
    if n <= 0:
        return
    result = ['0'] * n
    # if len(result) == 1:
    get_0_9(result,0)


def get_0_9(result, index):
    if len(result) == index:
        print_num(result)
        return
    for j in range(10):
        result[index] = str(j)
        get_0_9(result, index+1)


def print_num(result):
    index_i = 0
    while result[index_i] == '0' and index_i != len(result) - 1:
        index_i += 1
    print ''.join(result[index_i:])


if __name__ == '__main__':
    n = input("请输入位数n:")
    get_value(n)
