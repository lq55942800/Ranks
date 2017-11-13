# coding=utf-8
"""
选择排序
"""

import RandomNum

def SelectSort(L):
    L_len = len(L)
    for i in range(L_len):
        for j in range(i+1,L_len):
            if L[i]>L[j]:
                L[i],L[j] = L[j],L[i]
    return L

if __name__ == '__main__':
    L = RandomNum.Random_Num(10)
    list = SelectSort(L)
    print(list)
