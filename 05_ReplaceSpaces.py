#!/usr/bin/python
# -*- coding: UTF-8 -*-
def find(test):
    num = 0;
    for i in test:
        if i == ' ':
            num = num+1;
    out_len = len(test) + num*2;
    out = out_len * [None];
    i = len(test) -1;
    j = out_len - 1;
    while i >= 0:
        if test[i] != ' ':
            out[j] = test[i];
            j -= 1;
            i -= 1;
        else:
            out[j-2:j+1] = ['%', '2', '0'];
            j -= 3;
            i -= 1;
    return ''.join(out);

if __name__ == '__main__':
    test = "we are happy."
    print find(test);