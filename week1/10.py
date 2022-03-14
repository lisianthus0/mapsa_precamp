message = "Babak KKhorRRamdinR"

print(f"A = {message[0]}")
print(f"B = {message.find('K')}")
print(f"C = {message.rsplit(' ',1)}")
print(f"D = {message[0:12:2]}")
print("============================")

def strng(a = input("ye charcter bego : ")):
    counter = message.count(a)
    z = ([r for r,chr in enumerate(message) if chr == a])
    if a in message :
        if a.islower():
            print(f"E = in character {counter} bar tekrar shode va dar index {z} gharar darad")
        else:
            print(f"E = in character {counter} bar tekrar shode va dar index {z} gharar darad")
strng()