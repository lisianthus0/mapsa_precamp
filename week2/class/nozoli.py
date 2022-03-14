a = [1,8,12,9,1,5,12,21,3,4,9,2,5]
l = []
ls = []
l_index = []

for i in range(len(a)-1):
    if i==0:
        l.append(1)
    elif a[i]>a[i-1]:
        l.append(1)
    else:
        l.append(0)

for i in range(len(l)):
    if l[i]==0:
        ls.append(i)

for i in range(len(ls)-1):
    if ls[i] == ls[i+1]-1:
        l_index.append(i+1)

for i in range(len(l_index)-1, -1, -1):
    ls.pop(l_index[i])
print(ls)






