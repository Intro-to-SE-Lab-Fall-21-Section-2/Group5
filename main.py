from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formataddr
from flask_mail import Mail, Message
from flask import Flask, request, abort

import smtplib
import time
import imaplib
import email
import traceback
import sys
import os

app = Flask(__name__)

# Email
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='msuwebmail1@gmail.com'
app.config['MAIL_PASSWORD']= 'asdf1AB!'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL'] = True
mail=Mail(app)
username="msuwebmail1@gmail.com"
gmail_host='imap.gmail.com'


@app.route('/')
def index():
    while True:
        print("MSU WEBMAIL")
        print("-------------")
        print("Menu")
        print("1. Send Mail")
        print("2. Read Mail")
        print("3. Exit")
        print("-------------")
        choice=int(input("Enter your Choice:"))
        if choice==1:
             #os.system('cls' if os.name =='nt' else 'clear')
             recipient=input("Send to:")
             subject=input("subject:")
             body=input("body:")


             msg=Message(subject,sender='msuwebmail1@gmail.com',
                     recipients=[recipient])
             msg.body=body
             mail.send(msg)
             return 'Sent'

             index()
        if choice==2:
            break
  #           mail = imaplib.IMAP4_SSL(gmail_host)
  #           mail.login(username,"asdf1AB!")
  #           mail.select('INBOX')
             #select specific mails
  #           _, selected_mails = mail.search(None, '(FROM "msuwebmail1@gmail.com")')

#total number of mails from specific user
#print("Total Messages from msuwebmail1@gmail.com:" , len(selected_mails[0].split()))

#for num in selected_mails[0].split():
  #  _, data = mail.fetch(num , '(RFC822)')
  #  _, bytes_data = data[0]

    #convert the byte data to message
  #  email_message = email.message_from_bytes(bytes_data)
  #  print("\n===========================================")

    #access data
  #  print("Subject: ",email_message["subject"])
  #  print("To:", email_message["to"])
  #  print("From: ",email_message["from"])
  #  print("Date: ",email_message["date"])
  #  for part in email_message.walk():
  #      if part.get_content_type()=="text/plain" or part.get_content_type()=="text/html":
  #          message = part.get_payload(decode=True)
  #          print("Message: \n", message.decode())
  #          print("==========================================\n")
  #          break
                    #print(str(e))
  #          index()
        if choice==3:

            # os.system('cls' if os.name =='nt' else 'clear')
             sys.exit()
        else:

            # os.system('cls' if os.name =='nt' else 'clear')
             print("Wrong Choice")



if __name__ == '__main__':
    app.run(debug=True)
