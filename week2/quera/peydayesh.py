num_list = []
choice_list = list(range(1,5))
while len(num_list)<3:
    inpt = int(input("enter number: "))
    if inpt not in choice_list:
        print("ye adad dar reng 1 ta 4 bego")
        continue
    if inpt not in num_list:
        num_list.append(inpt)
print(f"==============\nchosed your number is {num_list}\ngues number is {set(choice_list).difference(num_list)}")