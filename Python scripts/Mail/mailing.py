Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import smtplib

>>> conn = smtplib.SMTP('smtp.gmail.com',587)
>>> type(conn)
<class 'smtplib.SMTP'>
>>> conn
<smtplib.SMTP object at 0x0207A580>
>>> conn.ehlo() #Function to start connection
(250, b'smtp.gmail.com at your service, [190.198.91.232]\nSIZE 35882577\n8BITMIME\nSTARTTLS\nENHANCEDSTATUSCODES\nPIPELINING\nSMTPUTF8')
>>> conn.starttls()
(220, b'2.0.0 Ready to start TLS')
>>> conn.login('somethingc@gmail.com','aadadAaa') #Requires device's password specific generation
smtplib.SMTPAuthenticationError: (535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials c11sm2037165qkb.58 - gsmtp')
>>> conn.sendmail('example@gmail.com','example2@hotmail.com','Subject: So long..\n\nDear Al,\n So long, and thanks for nothing') #from, to, mail's body
>>> conn.quit()
(221, b'2.0.0 closing connection c11sm2037165qkb.58 - gsmtp')
>>> 