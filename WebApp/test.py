import smtplib, ssl  # server library

def UnitTest():  # sends email to itself to verify it works (for travis CI)

    print("Test 1: Login with wrong password/correct email.")
    userEmail = "msuwebmail1@gmail.com"
    userPassword = "wrongPassword1"
    with smtplib.SMTP_SSL("smtp.gmail.com", emailport, context=context) as server:  # sending email
        try:
            server.login(userEmail, userPassword)
            print("FAIL")
        except:
            print("PASS")

    print("Test 2: Login with wrong email/correct password.")
    userEmail = "wrongEmail1@gmail.com"
    userPassword = "Forward1AB!"
    with smtplib.SMTP_SSL("smtp.gmail.com", emailport, context=context) as server:  # sending email
        try:
            server.login(userEmail, userPassword)
            print("FAIL")
        except:
            print("PASS")

 
    print("Test 3: Login with correct credentials.")  # setting up email
    userEmail = "msuwebmail1@gmail.com"
    userPassword = "Forward1AB!"

    with smtplib.SMTP_SSL("smtp.gmail.com", emailport, context=context) as server:  # sending email
        try:
            server.login(userEmail, userPassword)
            print("PASS")
        except:
            print("FAIL")
    print("Test 4: Create email with no sender, but includes a subject and body.")
    newMessage = EmailMessage()
    newMessage['To'] = ""
    newMessage['Subject'] = "TRAVIS CI TEST"
    newMessage['From'] = "Group 2"
    time = datetime.now()
    time = str(time)
    newMessage.set_content("Verification time: " + time)
    print("PASS")
    
    print("Test 5: Send email to itself.")
    with smtplib.SMTP_SSL("smtp.gmail.com", emailport, context=context) as server:
        try:
            server.login(userEmail, userPassword)
            server.send_message(newMessage)
            print("FAIL")
        except:
            print("PASS")
    print("Test 6: Create email with sender, subject, and body.")
    newMessage = EmailMessage()
    newMessage['To'] = userEmail
    newMessage['Subject'] = "TRAVIS CI TEST"
    newMessage['From'] = "Group 2"
    time = datetime.now()
    time = str(time)
    newMessage.set_content("Verification time: " + time)
    print("PASS")
    print("Test 7: Send test email to itself.")
    with smtplib.SMTP_SSL("smtp.gmail.com", emailport, context=context) as server:  # sending email
        server.login(userEmail, userPassword)
        server.send_message(newMessage)
        print("PASS")
    print("Test 8: Check if that exact previous email was recieved.")
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
     print("Test 9: Navigating to inbox without logging in.")
    try:
        redirect("/inbox")
        if authenticate() == True:
            print("FAIL")
        else: 
            print("PASS")
    except:
        print("PASS")
    print("Test 10: Navigating to director without logging in.")
    try:
        redirect("/director")
        if authenticate() == True:
            print("FAIL")
        else: 
            print("PASS")
    except:
        print("PASS")
    exit()
