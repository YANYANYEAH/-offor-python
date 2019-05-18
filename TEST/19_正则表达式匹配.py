# -*- coding:utf-8 -*-
# // 面试题19：正则表达式匹配
# // 题目：请实现一个函数用来匹配包含'.'和'*'的正则表达式。模式中的字符'.'
# // 表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题
# // 中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"
# // 和"ab*ac*a"匹配，但与"aa.a"及"ab*a"均不匹配。


# 正面暴力深度优先搜索，时间复杂度O(n^3)
# def get_equal(a,b,i,j):
#     if i < len(a) and j >= len(b):
#         return False
#     if i >= len(a) and j >= len(b):
#         return True
#     if i < len(a) and j + 1 < len(b) and b[j + 1] == '*':
#         if b[j] == a[i] or b[j] == '.':
#             return get_equal(a, b, i + 1, j + 2) or get_equal(a, b, i, j + 2) or get_equal(a, b, i + 1, j)
#         else:
#             return get_equal(a, b, i, j + 2)
#     if i < len(a) and (a[i] == b[j] or b[j] == '.'):
#         return get_equal(a, b, i+1, j+1)
#     if i == len(a) and j < len(b):
#         if j+1 < len(b) and b[j+1] == '*':
#             return get_equal(a, b, i, j + 2)
#         else:
#             return False
#     return False


# 倒着深度优先搜索
def get_equal(a,b,i,j):
    if i < 0 and j < 0:
        return True
    if i >= 0 and j < 0:
        return False
    if i >= 0 and b[j] == '*':
        if a[i] == b[j-1]:
            return get_equal(a,b,i-1,j) or get_equal(a,b,i-1,j-2)
        else:
            return get_equal(a,b,i,j-2)
    if i>=0 and a[i]==b[j] and b[j] == '.':
        return get_equal(a,b,i-1,j-1)
    if i<0 and j >= 0:
        if j-1>=0 and b[j] == '*':
            return get_equal(a,b,i,j-2)
    return False


if __name__ == '__main__':
    a = raw_input("a:")
    b = raw_input("b:")
    print get_equal(a,b,len(a)-1,len(b)-1)