# author: Rafael Salimov // https://github.com/thesaintraphael

import smtplib
import ssl
import sys

smptp_server = 'smtp.gmail.com'
port = 587      # for that server
password = input("Enter your password: ")

context = ssl.create_default_context()    # creates secure SSl context

sender = 'sender@gmail.com'
receiver = 'receiver@gmal.com'

#   subject have to be in the first line after '/' sign

message = '''\
Subject: Testing process of sending mails via Python

Hi Rafael. I sent that message by using Python module smtp.
That is just test mail, so you do not have to reply this message here.
Just inform me on WhatsApp, if you get message.

From Rafael Salimov.

Thank you!

'''

try:
    server = smtplib.SMTP(smptp_server, port)
    server.ehlo()   # enable connecting to server
    server.starttls(context=context)  # secures the connection
    server.login(sender, password)
    server.sendmail(sender, receiver, message)
    print('Your mail is sent successfully.')
except Exception as e:
    sys.stderr.write("A problem occured: ")
    sys.stderr.flush()
    print(e)

finally:
    server.quit()


'''

Note:

You have to allow less secure apps on chrome, otherwise Google will block your attempt to send an e-mail: myaccouns.google.com/lesssecureapps

'''
