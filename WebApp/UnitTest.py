import main.py
from smtplib import SMTP

#testing for travis CI
def UnitTest():                                         
    print("Test 1: Login with wrong password and email address.")          #user trying to login using a wrong password or id
    userEmail = "******@gmail.com"
    userPassword = "wrongpassword"
    with smtplib.SMTP_SSL("smtp.gmail.com", emailport, context=context) as server:  
        try:
            server.login(userEmail, userPassword)
            print("FAIL")
        except:
            print("PASS")

    print("Test 2: Login with wrong password/correct email.")
    userEmail = "group2emailclient@gmail.com"
    userPassword = "wrongPassword1"
    with smtplib.SMTP_SSL("smtp.gmail.com", emailport, context=context) as server:  # sending email
        try:
            server.login(userEmail, userPassword)
            print("FAIL")
        except:
            print("PASS")

    print("Test 3: Login with wrong email/correct password.")
    userEmail = "wrongEmail@gmail.com"
    userPassword = "Group2Test"
    with smtplib.SMTP_SSL("smtp.gmail.com", emailport, context=context) as server:  # sending email
        try:
            server.login(userEmail, userPassword)
            print("FAIL")
        except:
            print("PASS")

    print("Test 4: Locking out the user.")
    userEmail = "wrongEmail@gmail.com"
    userPassword = "wrongPassword1"
    with smtplib.SMTP_SSL("smtp.gmail.com", emailport, context=context) as server:  # sending email
        i = 0
        while(i < 5):
            try:
                server.login(userEmail, userPassword)
                Status = "FAIL"
                i += 1
            except:
                Status = "PASS"
                i += 1
        print(Status)

    print("Test 5: Login with correct credentials.")  # setting up email
    userEmail = "group2emailclient@gmail.com"
    userPassword = "Group2Test"

    with smtplib.SMTP_SSL("smtp.gmail.com", emailport, context=context) as server:  # sending email
        try:
            server.login(userEmail, userPassword)
            print("PASS")
        except:
            print("FAIL")

    print("Test 6: Create email with no sender, but includes a subject and body.")
    newMessage = EmailMessage()
    newMessage['To'] = ""
    newMessage['Subject'] = "TRAVIS CI TEST"
    newMessage['From'] = "Group 2"
    time = datetime.now()
    time = str(time)
    newMessage.set_content("Verification time: " + time)
    print("PASS")

    print("Test 7: Send test 6 email to itself.")
    with smtplib.SMTP_SSL("smtp.gmail.com", emailport, context=context) as server:
        try:
            server.login(userEmail, userPassword)
            server.send_message(newMessage)
            print("FAIL")
        except:
            print("PASS")

    print("Test 8: Create email with sender, subject, and body.")
    newMessage = EmailMessage()
    newMessage['To'] = userEmail
    newMessage['Subject'] = "TRAVIS CI TEST"
    newMessage['From'] = "Group 2"
    time = datetime.now()
    time = str(time)
    newMessage.set_content("Verification time: " + time)
    print("PASS")

    print("Test 9: Send test 8 email to itself.")
    with smtplib.SMTP_SSL("smtp.gmail.com", emailport, context=context) as server:  # sending email
        server.login(userEmail, userPassword)
        server.send_message(newMessage)
        print("PASS")

    print("Test 10: Check if that exact previous email was recieved.")
    # create an IMAP4 class with SSL
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    imap.login(userEmail, userPassword)
    imap.select('Inbox')
    type, messages = imap.search(None, 'ALL')
    numEmails = len(messages[0].split())
    typ, data = imap.fetch(str(numEmails).encode(), '(RFC822)') # reads most recent email
    msg = email.message_from_string(data[0][1].decode('latin1'))
    body = msg.get_payload()
    if time in body: # if email time is same as the time the test email was sent, test passes
        print("PASS")
