# coding=utf-8
"""
瞎想的
"""

import RandomNum

def MySort(list):
    list_len = len(list)
    New_list = []
    New_list.append(list[0])
    for i in range(1,list_len):
        if len(New_list) == 1:
            if list[i] >= New_list[0]:
                New_list.insert(1,list[i])
            else:
                New_list.insert(0,list[i])
        else:
            for j in range(len(New_list)):
                if list[i] <= New_list[0]:
                    New_list.insert(0,list[i])
                    break
                elif list[i] >= New_list[-1]:
                    New_list.append(list[i])
                    break
                elif list[i] >= New_list[j] and list[i] <= New_list[j + 1]:
                    New_list.insert(j + 1, list[i])
                    break
                else:
                    pass
    return New_list

if __name__ == '__main__':
    # L = RandomNum.Random_Num(5)
    L = [8,2,7,9,0,789,4432,13,4354,876,3253]
    list = MySort(L)
    print(list)