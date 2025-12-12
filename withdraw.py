from table import users_table
from Singleemailsender import single_email_sender
#withdraw function
def withdraw(account:int,withdraw_amount:int):
    #print("Withdraw page")
    #checking acc in users or not
    if account in users_table:
         amount=users_table[account][0]
         #checking amount is sufficent or not
         if amount>=withdraw_amount:
              users_table[account][0]-=withdraw_amount
              #print(f"{withdraw_amount} withdraw successful and current balance is:{users_table[account][0]}")
              user_email = users_table[account][2]
              subject = "about with_draw amount and current blence"
              body = f"{withdraw_amount} withdraw successful and current balance is:{users_table[account][0]}"
              single_email_sender(to_email=user_email,subject=subject,body=body)
              print("Email sent successfully")
         else:
              print("Insufficient amount in your account")
    else:
         print("user not found")