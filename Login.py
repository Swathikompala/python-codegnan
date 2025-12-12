from table import users_table
from table import accounts_table
def login(username:int,password:int):
    ##print("Login Page")
    #checking the account in account table or not
    if username in accounts_table:
        #checking the password
        if password==accounts_table[username]:
            print("login successfull")
            return True
        else:
            print("check with your credentials")
            return False
    else:
        print("user Not Found")