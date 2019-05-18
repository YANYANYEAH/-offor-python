# -*- coding:utf-8 -*-
# // 面试题11：旋转数组的最小数字
# // 题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
# // 输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如数组
# // {3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋转，该数组的最小值为1。

# 只要数据为顺序的或者部分顺序的——>二分查找


def get_min(a,index_1,index_2):
    if a[index_1] < a[index_2]:
        return a[index_1]
    index_mid = (index_1 + index_2) / 2
    if index_1 + 1 != index_2:
        if a[index_1] == a[index_mid] and a[index_mid] == a[index_2]:
            temp = a[index_1]
            for i in range(index_1+1, index_2):
                if a[i] < temp:
                    temp = a[i]
            return temp
        elif a[index_1] < a[index_mid]:
            return get_min(a, index_mid, index_2)
        elif a[index_1] >= a[index_mid]:
            return get_min(a, index_1, index_mid)

    else:
        return a[index_2]


if __name__ == '__main__':
    a = [1, 0, 1, 1, 1]
    print get_min(a, 0, len(a)-1)