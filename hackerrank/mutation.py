def mutate_string(string, position, character):
    l = list(string)
    l[int(position)] = character
    chng_str="".join(l)
    return chng_str

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)