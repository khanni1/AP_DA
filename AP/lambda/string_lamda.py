#rev , length, uppercase
a = "Khanjan"

reverse = lambda x: x[::-1] 

print(reverse(a))

length = lambda x: len(x)

print(length(a))

Uppercase = lambda x: x.upper()

print(Uppercase(a))
# Find highest the frequency of a character in a string 
text = "khanjan is Great python programmer goooddd"

freq = lambda s: max(set(s)-{" "},key=lambda ch: s.count(ch))

print(freq(text))

# Count a number of vowels in strings  
s = "khanjan is a AI ML engineer"
s2 = "AaEeIiOoUu"

vow = lambda s:sum(map(lambda ch:1 if ch.lower() in "aeiou" else 0,s))

print(vow(s2))

# Check Palindrome from string 
ispalin = lambda s: s == s[::-1]

print(ispalin("level"))



