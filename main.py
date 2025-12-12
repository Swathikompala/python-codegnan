import Login
import withdraw
import Deposit
import Transfer
import BalanceEnquiry
import Logout
import ministatement

if __name__ == "__main__":
    print("Welcome to the bank")
    username=int(input("Enter your account number:"))
    password=int(input("Enter your password :"))
    login_val=Login.login(username=username,password=password)
    while login_val:
        operations=("1.withdraw \n",
                        "2. deposit \n",
                        "3.transfer \n",
                        "4. ministatement \n",
                        "5.Blance enquiry \n"
                        "6.logout \n")
        print(*operations)
        choice=int(input("select your operation"))
        if choice==1:
                withdraw.withdraw(account=username,withdraw_amount=int(input("Enter withdraw amount")))
        elif choice==2:
                Deposit.deposit(account=username,deposit_amount=int(input("Enter deposit amount")))
        elif choice==3:
                Transfer.transfer(sender=username,reciver=int(input("enter the account number")),transfer_ammount=int(input("enter transfer amount")))
        elif choice==4:
                ministatement.mini_statement(account=username)
        elif choice==5:
                BalanceEnquiry.blance_enquiry(account=username)
        elif choice==6:
                Logout.logout(username)
        else:
                print("Select your operation in Between 1 to 5 ")