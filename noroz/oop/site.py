from account import Account

class Site():
    def __init__(self, url, registered_users = [], active_users = []):
        self.url = url
        self.registered_user = registered_users
        self.active_user = active_users
    def register(self,user):
        self.registered_user.append(user.username)
    def login(self,user):
        use = input("username: ")
        pss = hash(input("password:"))
        for i in self.registered_user:
            if use == i:
                if pss == user.password:
                    print("welcome")


a = Account("amir_mohammadi","Aa300b540","09123326623","mohammadiamir00@gmail.com")
b = Site("urls")
(b.register(a))
(b.login(a))
print(b.registered_user)

