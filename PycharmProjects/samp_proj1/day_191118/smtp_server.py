# import the smtplib module. It should be included in Python by default
import smtplib

# set up the SMTP server
s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login("poornima.d@hcl.com","Ramahanuman3")