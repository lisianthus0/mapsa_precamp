from random import randint
pc = randint(1,10)
user = int(input("ye adad bego: "))
count = 0
while user!=pc:
    print(f"eshtebah gofti . {count+1}/5 forsat")
    if count==5:
        break
    elif user<pc:
        print("boro bala tar")
    else:
        print("boro pain tar")
    count+=1
    user = int(input("ye adad beg: "))
if user==pc:
    print(f"barande shodi\n")
else:
    print(f"Game over.\nYou {user} VS PC {pc}")
