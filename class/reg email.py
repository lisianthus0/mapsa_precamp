import re

print(re.match(r"([a-zA-Z0-9]+)@([a-zA-Z]+)\.([a-z]{2,3})","mohammadiamir00@gmail.com").groups())

print(re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)","mohammadiamir00@gmail.com").groups())


