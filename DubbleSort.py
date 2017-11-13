# coding=utf-8
"""
冒泡排序
"""
import RandomNum

def DubbleSort(L):
    L_len = len(L)
    for i in range(L_len):
        for j in range(L_len - i - 1):
            if L[j] > L[j + 1]:
                L[j], L[j + 1] = L[j + 1], L[j]
    return L


if __name__ == '__main__':
    L = RandomNum.Random_Num(20)
    list = DubbleSort(L)
    print(list)
