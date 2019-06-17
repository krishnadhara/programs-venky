a = ['ashok', 'hari', 'bhanu', 'anil', 'bharath', 'anvesh', 'uday', 'raja']
d = {}
for i in a:
    s = i.split()
    if s[0] not in d:
        d[s[0][0]] = []
    d[s[0][0]].append(s[0])
print(d)