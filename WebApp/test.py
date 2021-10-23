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

    print("Test 2: Locking out the user.")
    userEmail = "wrongEmail123@gmail.com"
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

    print("Test 3: Login with correct credentials.")  # setting up email
    userEmail = "msuwebmail1@gmail.com"
    userPassword = "Forward1AB!"

    with smtplib.SMTP_SSL("smtp.gmail.com", emailport, context=context) as server:  # sending email
        try:
            server.login(userEmail, userPassword)
            print("PASS")
        except:
            print("FAIL")

    
