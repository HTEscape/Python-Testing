import smtplib

gmail_user = 'crinc.alarms@gmail.com'
gmail_password = 'Alarm123'

def send_email(to_address, subject, body):
    sent_from = gmail_user
    to_string = 'To: '
    if isinstance(to_address, str):
        to_string += to_address
    elif isinstance(to_address, list):
        for i in range(len(to_address)):
            to_string += to_address[i]
            if i < (len(to_address) - 1):
                to_string += ', '
    else:
        return "You did not supply a list or string for the to address"

    email_text = '%s\nSubject: %s\n%s' % (to_string, subject, body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print('Email sent!')
        print(email_text)
    except:
        print('Something went wrong...')


to = ['chadwr@sbcglobal.net', '8054044713@txt.att.net', 'chad.robbins@spectrumbrands.com', 'chadwremail@gmail.com']
subject = 'Function with parameters'
body = 'I have changed the function to make it more flexible in my programs'
print(send_email(to, subject, body))