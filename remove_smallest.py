#coding=utf-8

class removeSmallest:
    def __init__(self,list):
        self.list = list
    def remove_smallest(self):
        num_min = min(list)
        count_min = list.count(num_min)
        List_index = []
        List_value = []
        List_min = []
        for index,value in enumerate(list):
            List_index.append(index)
            List_value.append(value)
        if count_min > 1:
            for i in List_index:
                if List_value[i] == num_min:
                    List_min.append(i)
            list.pop(List_min[0])
        else:
            for i in List_index:
                if List_value[i] == num_min:
                    list.pop(i)
        return list

if __name__ == '__main__':
    list = [1,2,3,5]
    removeSmallest = removeSmallest(list)
    print(removeSmallest.remove_smallest())
