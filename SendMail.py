#This is a python script which uses smtp library in order to send emails in bulk. This script will work only if 
#lesssecureapps is enabled on google setting. Use the link below to allow lesssecureapps.
# https://myaccount.google.com/lesssecureapps


#This is a dictionary to save name and email.
friends = {
    'Kamal Tripathi':  'kamaltri123@gmail.com',
    'kamalt':          'kamalt@imsc.res.in'
} 



SUBJECT               = 'This is subject of the email'
SALUATION             = 'Dear '
MAINBODY              = '\nI have an announcement to make. This is an automated message sent by pyhton.'
COMPLIMENTARY_CLOSING = '\n \nSincerely, \nKamal Tripathi.'

#keep email password in password.txt file.
with open('password.txt') as f:
    password=f.read()
    
import smtplib

for NAME in friends:
    BODY = SALUATION + str(NAME) + ',' + MAINBODY + COMPLIMENTARY_CLOSING
    message = 'Subject: {}\n\n{}'.format(SUBJECT, BODY)
    sm = smtplib.SMTP('smtp.gmail.com', 587)
    sm.ehlo()
    sm.starttls()
    sm.login('kamaltri123@gmail.com', password)
    sm.sendmail('kamaltri123@gmail.com', friends[NAME], message)
    sm.quit()

