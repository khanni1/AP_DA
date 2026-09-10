# My personal practice Q for lambda

# get a sorted list of words of a string sentence based on length of words

s = "Hello i am khanjan Learning Python AI"

sort_list = lambda s: sorted(s.split(),key=len)

print(sort_list(s))

# sort words of sentence on basis of their last character

s = "Mango Banana Grapes Khanjan Python za xb sc"

last_char_sort = lambda s:sorted(s.split(),key=lambda x: x[-1])

print(last_char_sort(s))

# find list of all keys which have a particular value in dictionary

d = {"khanjan" : 1,"Ramu" : 2,"Shamu" : 1}

find_keys = lambda d,val: [k for k,v in  d.items() if v == val]

print(find_keys(d,1))

        