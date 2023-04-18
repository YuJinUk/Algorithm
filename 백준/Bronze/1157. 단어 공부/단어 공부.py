from collections import Counter
a = input().upper()
key = list(Counter(a).keys())
val = list(Counter(a).values())

if val.count(max(val)) != 1:
    print('?')
    exit()

print(key[val.index(max(val))])