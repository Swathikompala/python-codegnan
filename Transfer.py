from table import users_table
from Singleemailsender import single_email_sender
#transfer function
def transfer(sender:int,reciver:int,transfer_ammount:int):
    #print("transfer page")
    #checking that sender and reciver present in users table or not
    if sender in users_table and reciver in users_table:
         if transfer_ammount<=users_table[sender][0]:
              users_table[sender][0]-=transfer_ammount
              users_table[reciver][0]+=transfer_ammount
              user_email = users_table[sender][2]
              subject = "about with_draw amount and current blence"
              body = f"{transfer_ammount} transfer successful and current balance is:{users_table[sender][0]}"
              single_email_sender(to_email=user_email,subject=subject,body=body)
              print("Email sent successfully")
              print(f"{transfer_ammount} transfer successful and current balance is:{users_table[sender][0]}")
         else:
              print("Insufficent balance in your account")
    else:
         print("User not found")