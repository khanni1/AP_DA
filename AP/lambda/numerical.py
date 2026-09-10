# cube root
value = lambda x: x**(1/3)

print(value(27))

#min of 2 
min = lambda a,b: a if a<b else b

print(min(5,9))

# longest word
Statement = "Today i am attending advance python lecture using lambda function"

large = lambda x: max(x.split(),key=len)

print(large(Statement))

# Write a lambda function to remainder of 2 number
x = lambda a,b: a%b

print(x(10,6))

# Find a factorial of 5 to 10
fact = lambda x: x*fact(x-1) if x != 0 else 1

for i in range(5,11,1):
    print(fact(i))
    
    
# List answer  will be second highest
lst1 = [10,20,320,10,430,102,43,500]

second_high = lambda lst: sorted(lst,reverse=True)[1]

print(second_high(lst1))

# Find the LCM of 2 numbers
# first find GCD
gcd = lambda a,b: a if b == 0 else gcd(b,a%b)

lcm = lambda a,b : (a*b) // gcd(a,b)

print("GCD : ",gcd(135,225))
print("LCM : ",lcm(135,225))

# Find the student with the highest result.(using dictonary)
students = {"Ramu" : 100,"Shamu" : 90,"Tamu" : 25,"Mamu" : 78, "Aura_man" : 100}

find_keys = lambda d,val: [k for k,v in  d.items() if v == val]

find_highest_marks = lambda d: find_keys(d,max(list(d.values())))

print(find_highest_marks(students))


