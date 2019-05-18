# -*- coding:utf-8 -*-
# 快速排序
# python一切皆引用，改变参数的值也会改变实参的。


def partion(aa, left, right):
    key = aa[left]
    while left < right:
        while left < right and aa[right] > key :
            right -= 1
        if left <right:
            aa[left], aa[right] = aa[right], aa[left]
        else:
            break
        while left < right and aa[left] < key :
            left += 1
        if left < right:
            aa[left], aa[right] = aa[right],aa[left]
        else:
            break
    return left


def quick_sort(a,left,right):
    if left < right:
        index = partion(a, left, right)
        quick_sort(a, index+1, right)
        quick_sort(a, 0, index-1)


if __name__ == '__main__':
    a = [5,6,4,2,3,1]
    quick_sort(a, 0, len(a)-1)
    print a