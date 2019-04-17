# -*- coding:utf-8 -*-

# // 面试题10：斐波那契数列
# // 题目：写一个函数，输入n，求斐波那契（Fibonacci）数列的第n项。
# 题目：一只青蛙一次可以跳上1级台阶，也可以跳上2级台阶。求该青蛙跳上一个n级的台阶总共有多少种跳法？


def get_f_n(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    # 如果是跳青蛙就加上！
    # elif x == 2:
    #     return 2
    else:
        a_2 = 2
        a_1 = 1
        for i in range(x+1-2):
            aa = a_1 + a_2
            a_2 = a_1
            a_1 = aa
        return aa

if __name__ == '__main__':
    x = input("请输入n：")
    print get_f_n(x)