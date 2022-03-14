
def swap_case(s):
    result = []
    if 0 < len(s) <= 1000:
        for i in s:
            if i.isalpha():
                if i.islower():
                    result.append(i.upper())
                elif i.isupper():
                    result.append(i.lower())
            else:
                result.append(i)
    return "".join(result)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)