a = [1, 2, 1, 3, 2, 3, 1, 2, 1]

b=0
d=1
f=2
c = []
while len(a)>b and len(a)>d:
    if a[b]<a[d]>a[f]:
        a[d]=a[f]
    b+=1
    d+=1
    f+=1

print(a)



















# l1 = [2,1,3,1,3,1,3,1,3]
# lb = l0[1:len(l0)-1]
# lr = []
