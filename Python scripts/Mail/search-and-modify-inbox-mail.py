Python 3.8.3 (tags/v3.8.3:6f8c832, May 13 2020, 22:20:19) [MSC v.1925 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # pip install imapclient // pip install pyzmail
>>> import imapclient
>>> conn= imapclient.IMAPClient('imap.gmail.com', ssl=True) #True to use SSL encryption
>>> conn.login('example2@mail.com','whatever')
>>> conn.select_folter('INBOX',readonly= True)

>>> UIDs = conn.search(['SINCE 20-Aug-2015']) #return a list of unique IDs for mails
>>> rawMessage=conn.fetch(['mail int UID number to fetch'],['BODY[]','FLAGS'])

>>> import pyzmail

>>> pyzmail.PyzMessage.factory(rawMessage['same UID Number passed to rawMessage'][b'BODY'])

>>> message=pyzmail.PyzMessage.factory(rawMessage['same UID Number passed to rawMessage'][b'BODY'])
T
>>> message.get_subject() #mail's subject

>>> message.get_addresses('from')

>>> message.get_addresses('to')

>>> message.get_addresses('bcc')

>>> message.text_part # return len and type

>>> message.text_part #None if doesn't have html

>>> message.html_part == None # True

>>> message.text_part.get_payload().decode('UTF-8')

>>> message.text_part.charset

>>> conn.list_folders()

>>> conn.select_folder('INBOX',readonly=False) #to modify the inbox

>>> UIDS= conn.search(['ON 24-Aug-2015'])

>>> conn.delete_messages(['UIDs to delete'])

>>> ''' Full documentation ar: https://imapclient.readthedocs.org http://www.magiksys.net/pyzmail '''