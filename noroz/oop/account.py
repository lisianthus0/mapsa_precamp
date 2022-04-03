import re
class Account:
    def __init__(self,username,password,phonenumber,email):
        if re.match("^[a-zA-Z_]*$",username) is None:
            print("Moshkel dare")
        else:
            self.username = username
        if re.match("(?=^.{8,}$)(?=.*[A-Z])(?=.*[a-z])(?=.*[1-9]).*$",password) is None:
            print("Moshkel dare")
        else:
            self.password = hash(password)
        if re.match("^\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *x(\d+))?\s*$",phonenumber) is None:
            print("Moshkel dare")
        else:
            self.phonenumber = phonenumber
        if re.match("^([\w\.\_]+)@([\w\-]+)((\.(\w){2,3})+)$",email) is None:
            print("Moshkel dare")
        else:
            self.email = email




