

d = dict()
v = set()

a = [0,1,2,3,4,5]

for b in a:
    for x in a:
        if b!=x and (x,b) not in v and reversed(tuple((x,b))) not in v:
            v.add((b,x))
            d[b,x]=1 
print(d)

output, seen = [], set()
for item in d:
    t1 = tuple(item)
    if t1 not in seen and tuple(reversed(item)) not in seen:
        seen.add(t1)
        output.append(item)

print(output)
