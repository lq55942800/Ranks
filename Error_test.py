
def my_abs2(y):
    if not isinstance(y,(float,int)):
        raise TypeError('bad operand type')
    # if y>=0:
    #     return(y)
    # else:
    #     return(-y)

def a_insert():
    a = [2,3,4,5]
    a.insert(1,0)
    return a

l = a_insert()
print(l)