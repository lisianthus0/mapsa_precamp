import csv
from collections import defaultdict


def filter(a):
    dic = defaultdict(list)
    with open('esm_famil_data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            for key, value in line.items():
                dic[key].append(value)

    for key, value in dic.items():
        dic[key]=[i for i in value if len(i)>0]

    for key, value in dic.items():
        dic[key]=[j for j in value if j[0] == a]
    return dic

# print(filter("ا"))

def users():
    a = int(input("chand nafar: "))
    users= {}
    while a>0:
        user = input("whats your name: ")
        while len(user)==0:
            print("requirement")
            user = input("whats your name: ")
        l = ["esm", "famil", "keshvar", "rang", "ashia", "ghaza"]
        answers = {}
        for i in l:
            answer = {i: input(f"{i}: ")}
            answers.update(answer)
        users.update({user: answers})
        a-=1
    return users

# print(users())


"""
if all user answer:
    if one user answer not in dic or Non > 0
    if all user answer once > 5
    if all user different answer > 10
if user not answer:
    if not in dic or Non > 0
    if other user answer once > 10
    if user just answer > 15
     

"""
a = {'امیر': {'esm': 'امیر', 'famil': 'امیری', 'keshvar': 'امریکا', 'rang': 'ابی', 'ashia': 'الک', 'ghaza': 'ابگوشت'}, 'شادی': {'esm': 'ارمان', 'famil': 'امینی', 'keshvar': 'ایران', 'rang': '', 'ashia': 'ابر', 'ghaza': 'ابگوشت'}, 'مصی': {'esm': 'اتنا', 'famil': 'امیری', 'keshvar': 'انگولا', 'rang': '', 'ashia': 'ابکش', 'ghaza': 'البالو پلو'}}
