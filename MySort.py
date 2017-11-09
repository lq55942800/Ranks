# coding=utf-8
"""
瞎想的
新建一个newlist,把需要排序的list第一个元素拿出来存进去，然后取list第二个数，如果大于newlist的数就放第一位，小于就放第二位。
然后取第三个，与newlist的数字进行比较(此时newlist的数字是按顺序放的)，如果小于list[0]就插入到newlist最前端，如果大于list[-1]就插入到最后端，
如果位于两数字之间，就插入其中。
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
    L = RandomNum.Random_Num(5)
    list = MySort(L)
    print(list)
