# coding=utf-8
'''
生成随机数组
'''

import random

L = []


def Random_Num(num):
    for i in range(num):
        L.append(random.randint(0, 9999))
    return L
