y=(3>4)
def my_abs2(y):
 if not isinstance(y,(float,int)):
  raise TypeError('bad operand type')
 if y>=0:
  return(y)
 else:
  return(-y)

print(my_abs2(y))