import smtplib#simple email transfer protocal
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
# sender details
SENDER_EMAIL="kompalaswathi054@gmail.com"
SENDER_PASSKEY="mpxx lzjf ykqw qvse" 
SMTP_SERVER="smtp.gmail.com"
SMTP_PORT=587
# single email sender function
def single_email_sender(to_email:str,subject:str,body:str):
    msg=MIMEMultipart()
    msg["TO"]=to_email
    msg["From"]=SENDER_EMAIL
    msg["Subject"]=subject
    msg.attach(MIMEText(body,"html"))
    #create server connection
    try:
        server=smtplib.SMTP(SMTP_SERVER,SMTP_PORT)
        # server starts sequerly
        server.starttls()
        #login to server
        server.login(SENDER_EMAIL,SENDER_PASSKEY)
        #send email to  to_email
        server.sendmail(SENDER_EMAIL,to_email,msg=msg.as_string())
        #server quit
        server.quit()
    except Exception as e:
        print(f"field to send email to {to_email}:,{e}")