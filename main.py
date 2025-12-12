from single_emai_sender import single_email_sender
from bulk_email_sender import bulkEmailSender
if __name__ == "__main__":
    print("Welcome to email sender using python")
    choice = int(input("1. single email sender \n 2. Bulk email sender \n \
                       Enter your operations : "))
    #reciever_email = input("Enter Reciever email: ")
    subject = input("Enter subject:")
    body = input("Enter body msg:")
    if choice == 1:
        reciever_email = input("Enter Reciever mails : ")
         #single body email function calling

        single_email_sender(to_email = reciever_email, subject = subject, body = body)
        print(f"{reciever_email} to Email send successfully")

    elif choice == 2:
        emails = input("Enter list of emails separated by comma:").split(",")
        emails = [e.strip() for e in emails]
        bulkEmailSender(list_of_emails = emails, subject = subject, body = body)
        print("Emails sent successfully to all recipients")
    else:
        print("select valid operations")