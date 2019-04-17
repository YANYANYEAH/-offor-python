# -*- coding:utf-8 -*-
# // 面试题16：数值的整数次方
# // 题目：实现函数double Power(double base, int exponent)，求base的exponent
# // 次方。不得使用库函数，同时不需要考虑大数问题。

# tips: 考虑特殊条件，比如 exponent 为负数， 此时结果需要取倒数
#                     当结果去倒数的时候，需要考虑分母为0的情况，0^n = 0或者1，n^0 = 1


# 此处需要考虑 简单的方法，比如a^n = a^(n/2) * a^(n/2)  此时需要考虑n为奇数还是偶数
# def get_result(base, exponent):
#     if exponent == 0:
#         return 1
#     elif exponent == 1:
#         return base
#     else:
#         if exponent%2 ==1:
#             result = get_result(base, exponent/2)
#             result = result * result * base
#         else:
#             result = get_result(base, exponent/2)
#         return result


# 此时考虑位运算，加速，每移一位相当于开方
def get_result(base, exponent):
    if exponent == 0:
        return 1
    elif exponent == 1:
        return base
    else:
        result = get_result(base, exponent >> 1)
        result *= result
        if exponent & 1 == 1:
            result *= base
        return result


def get_value(base, exponent):
    if base == 0:
        return 0
    elif exponent < 0:
        result = get_result(base,-exponent)
        return 1.0/result
    else:
        result = get_result(base, exponent)
        return result


if __name__ == '__main__':
    base = input("input base:")
    exponent = input("input exponent:")
    print get_value(base, exponent)