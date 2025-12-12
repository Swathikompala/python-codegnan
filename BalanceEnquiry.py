from table import users_table
from Singleemailsender import single_email_sender
#blance enquiry function defination
def blance_enquiry(account:int):
     if account in users_table:
          print(f"Current blance is:{users_table[account][0]}")
          user_email = users_table[account][2]
          subject = "about  current blance"
          body = f" current balance is:{users_table[account][0]}"
          single_email_sender(to_email=user_email,subject=subject,body=body)
          print("Email sent successfully")
     else:
        print("user not found")