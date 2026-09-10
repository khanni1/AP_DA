from functools import reduce

A = [2,4,6,8]
a = reduce(lambda x,y:x+y,A)
print(a)

B = [67,89,20,12]
b = min(B)

c = reduce(lambda x,y : x if x>y else y,B)

print(b)
