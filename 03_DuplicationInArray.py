#!/usr/bin/python
# -*- coding: UTF-8 -*-
def duplicate(test1):
    temp = 0;
    for i in range(len(test1)):
        if test1[i] > len(test1)-1 or test1[i]<0:
            return -2;
        else:
            if test1[i] == i:
                i= i+1;
                if i == len(test1):
                    return -1;
            else:
                if test1[i] == test1[test1[i]]:
                    return test1[i];
                else:
                    temp = test1[i];
                    test1[test1[i]] = temp;
                    test1[i] = test1[test1[i]];

if __name__ == '__main__':
    test1 = [2, 1, 3, 4, 4];
    print(duplicate(test1));
