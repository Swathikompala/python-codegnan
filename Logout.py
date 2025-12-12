from table import users_table
from Singleemailsender import single_email_sender
#logout function
def logout(username):
    user_email = users_table[username][2]
    subject = "about loging out and current balance"
    body = f"current balance is:{users_table[username][0]}Logout successfully"
    single_email_sender(to_email=user_email,subject=subject,body=body)
    print("Email sent successfully")
    exit()