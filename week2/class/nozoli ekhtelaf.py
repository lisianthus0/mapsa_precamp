a = [1,3,8,12,24,2,15,16,21]
b = [1,8,9,21,2,16]
def new(a:list):
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

    a_new = []
    for i in reversed(ls):
        a_new.append(a[i:])
        del a[i:]
        del i
    if len(a)!=0:
        a_new.append(a)
    list(reversed(a_new))
    d = []
    for i in a_new:
        d.append(set(i))
    return d

x = new(a)
y = new(b)
if len(x) == len(y):
    print("===orginal===")
    print(x)
    print(y)
    print("===difference===")
    print(x[0].difference(y[0]))
    print(x[1].difference(y[1]))
    print("===intersection===")
    print(x[0].intersection(y[0]))
    print(x[1].intersection(y[1]))
else:
    print("not match")
