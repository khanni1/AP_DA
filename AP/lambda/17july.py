from functools import reduce

# map Q
# grade for 1-100 marks of each student

lst = [10,45,67,89,43,100,98,34,23,86,34,76,34]

lst_grade = list(map(lambda x: 'A' if x >= 80 else('B' if x >= 60 else ('C' if x>=30 else 'D')),lst))

print(lst_grade)

# reduce Q
# concate all names in list
names = ["khanjan","kushal","ramu","tamu"]

a = reduce(lambda x,y:x+y,names)

print(a)

# MAX min using reduce

nums = [1,2,3,4,5,6,7,8,9,10,12,-9,5,4]

minx = reduce(lambda x,y: x if x<y else y,nums)

maxx = reduce(lambda x,y: x if x>y else y,nums)

print("max : ",maxx)
print("min : ",minx)

#GCD

find_gcd = [3,6,12]

gcd = lambda x,y : x if y == 0 else gcd(y,x%y)

gcd_all = reduce(lambda x,y: gcd(x,y),find_gcd)

print(gcd_all)

