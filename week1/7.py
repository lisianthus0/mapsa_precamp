a = range(20,201)
b = []
for i in a:
    if i%3!=0 and i%5==0:
        b.append(i)
    else:
        continue
print(list(reversed(b)))
