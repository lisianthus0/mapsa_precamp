import re
from itertools import product


def change(string): # فانکشنی که استرینگ ناقص را به انتخاب شما تکمیل میکند
    print(string)
    a = [pos for pos, char in enumerate(string) if char == "?"] #ایندکس هایی که ؟ داخلشون هست
    b = [i for i in string] # تبدیل استرینگ به لیست
    for i in a:
        b[i]=input("ye adad: ") # جایگزین کردن یک عدد به جای "?"
    return "".join(b) # تبدیل لیست تکمیل شده با اعداد انتخابی به استرینگ اولیه


def match(func): # فانکشنی مشخص میکند استرینگ تکمیل شده خوش تعریف است یا نه
    pattern = ["11","00"] # الگوهای ای که برای خوش تعریف بودن نباید باشن
    d = [] # لیستی که مشخص میکنه الگوهای مورد نظر داخل استرینگ هستن یا نه
    c = "" # جواب نهایی در اینجا ریخته میشه
    for i in pattern: # مشخص کردن وجود یا عدم وجود الگو های ممنوعه
        if re.search(i, func): # با استفاده از ماژول regx
            d.append(True)
        else:
            d.append(False)
    if any(d): # اگر یکی از اعضای داخل لیست d درست بود یعنی خوش تعریف نیست
        c = "khosh tarif nist"
    else:
        c = "khosh tarif hast"
    return c

print(match(change("01???10")))








#
# def match(integer):
#     suggestions = [integer.replace("?" * integer.count("?"), i) for i in ["".join(i) for i in list(product(['0','1'],repeat=integer.count("?")))]]
#     pattern = ["11","00"]
#     d = []
#     c = ""
#     for i in suggestions:
#         s = []
#         for j in pattern:
#
#             if re.search(j, i):
#                 s.append(True)
#             else:
#                 s.append(False)
#         d.append(s)
#     for i in d:
#         if any(i):
#             c = "khosh tarif nist"
#         else:
#             c = "khosh tarif hast"
#             break
#     return f"{integer}\n{suggestions}\n{pattern}\n{d}"
#
#
# print(match("01???1??0"))


