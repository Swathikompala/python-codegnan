from table import users_table
from Singleemailsender import single_email_sender
#deposit finction
def deposit(account:int,deposit_amount:int):
    #print("Deposit page")
    if account in users_table:
         if deposit_amount >0:
            users_table[account][0]+=deposit_amount
           # print(f"{deposit_amount} deposit successful and current balance is:{users_table[account][0]}")
            user_email = users_table[account][2]
            subject = "about deposit_amount and current balance"
            body = f"{deposit_amount} deposit successful and current balance is:{users_table[account][0]}"
            single_email_sender(to_email=user_email,subject=subject,body=body)
            print("Email sent successfully")
         else:
              print("Check with your deposit amount")
    else:
         print("user not found")