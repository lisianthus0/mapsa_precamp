i = 10038
p = input(f"dar adad {i} do adad ke dar hamsayegi ham hastand bego: ")


def shorten(integer,pattern):
    string = str(integer)
    if pattern in string:
        return string.replace(pattern,str(sum(map(int,[i for i in pattern]))))

print(shorten(i,p))











# def small(a,b,c):
#     z = [i for i in str(a)]
#     x = str(b)
#     y = str(c)
#
#     if z.index(x) == z.index(y)-1 or z.index(x) == z.index(y)+1:
#         z.remove(y)
#         z[z.index(x)]= str(int(x) + int(y))
#     return int("".join(z))
#
# print(small(a,0,3))