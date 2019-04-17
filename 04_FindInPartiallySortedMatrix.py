#!/usr/bin/python
# -*- coding: UTF-8 -*-
def findx(test,a):
    w = len(test);
    h = len(test[0]);
    i = 0;
    j = h-1;
    while(i<w and j>=0):
        if test[i][j] == a:
            return [i,j];
        elif test[i][j]>a:
            j = j-1;
        else:
            i = i+1;
    return [-1,-1]


if __name__ == '__main__':
    test = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]];
    print findx(test,1);