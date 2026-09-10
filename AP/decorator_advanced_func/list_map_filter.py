
print("hello")
strx = ["kushal","khanjan","ramu",]
a= list(map(lambda x : x.upper(),strx))
print(a)
b = list(map(lambda x :len(x),strx))
print(b)
num = [1,2,3,4,5]
num2 =[6,7,8,9,10]
c = list(map(lambda x,y : x+y,num,num2))
print(c)
num3 = [1.5608,2.3456,3.7890]
d = list(map(lambda x : round(x,3),num3))
print(d)
X = [1,2,3,4,5,6,7,8,9,10]
e = list(filter(lambda x : x%2==0,X))
print(e)
Y = [10,2,3,4,5,6,7,8,90,10]
f = list(filter(lambda x: x>5 ,Y))
print(f)
Z = ["kushal","khanjan","ramu","suresh","madam","level","radar"]
g = list(filter(lambda x: x==x[::-1],Z))
print(g)