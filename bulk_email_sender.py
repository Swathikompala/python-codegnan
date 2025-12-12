from single_emai_sender import single_email_sender

#bulk email send function defination

def bulkEmailSender(list_of_emails:list[str], subject : str, body : str):
    for email in list_of_emails:
        try:
            single_email_sender(to_email = email, subject = subject, body = body)
            print(f"{email} to email send successfully")
        except Exception as e:
            print(f"{email} to email send field")