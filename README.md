# RBPIMailbox
Python 3 script for a Raspberry Pi 2/3 based smart mailbox. Using an LCD screen, A lock and a mailbox to send notifications.

There are a few changes that have to be done before this works, mainly the changes to your mailserver to allow less secure apps to send emails. and entering the email you want in the python file. (For enabeling less secure apps in gmail read: https://support.google.com/accounts/answer/6010255)

Changes in the python file:
22: replace [code.txt] with the file where the barcodes you're expecting are located, each code on a different line. last line ending with +++END+++ (see example.txt)

42: replace [fromaddr] with the email address you want to send the notification email from
43: replace [toaddr] with the email address you want to recieve the notification email from

50: replace the email server with the server you want to use and the correct port. gmail is set as default
51: replace the email server with the server you want to use and the correct port. gmail is set as default

57: replace [Your email password] with the password of the email address from [fromaddr]

All steps will be displayed on the LCD 2X16 screen as feedback.
