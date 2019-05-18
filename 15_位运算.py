# -*- coding:utf-8 -*-
# // 面试题15：二进制中1的个数
# // 题目：请实现一个函数，输入一个整数，输出该数二进制表示中1的个数。例如
# // 把9表示成二进制是1001，有2位是1。因此如果输入9，该函数输出2。


# 最好的方法
def get_1_0(a):
    count = 0
    while(a):
        count += 1
        a = (a-1) & a
    return count


# 第一种方法，原始方法
def get_1_1(a):
    count = 0
    flag = 1
    while(flag<0xFFFFFFFF):
        if a&flag:                 # 注意&运算与*运算的区别
            count += 1
        flag = flag<<1
    return count


# 第一种方法，c++中错误的方法，但因为python中没有无符号数，负数前都有"-"，所以没有问题
def get_1_2(a):
    count = 0
    flag = 1
    while(a):
        if a&flag:                 # 注意&运算与*运算的区别
            count += 1
        a = a>>1
    return count


if __name__ == '__main__':
    a = input("请输入a:")
    print get_1_0(a)
    print get_1_1(a)
    print get_1_2(a)
