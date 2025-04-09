#Big fan btw. I decided to start submitting the answers instead of just letting them float around.
def isLongPressed(a, b):
    s_a = set(a)
    s_b = set(b)
    for char in s_b:
        if b.count(char) < a.count(char):
            return False
    return len(b) >= len(a) and s_b == s_a

print(isLongPressed("alex", "aaleex") == True)

print(isLongPressed("saeed", "ssaaedd") == False)

print(isLongPressed("leelee", "lleeelee") == True)

print(isLongPressed("Tokyo", "TTokkyoh") == False)

print(isLongPressed("laiden", "laiden") == True)

"""
Didn't seem required but if you add the part after 
s_b = ...

i = 0
for char in b:
    if i < len(a) and a[i] == char:
      i += 1
    if i != len(a):
      return False

It will check for the order of things:
print(isLongPressed("abc", "acbb") == False)
"""
