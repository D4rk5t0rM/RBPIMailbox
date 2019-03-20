import RPi.GPIO as GPIO #use the RBPI pins
import time
import sys
import smtplib

#subject
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#LCD
from RPLCD import CharLCD

#from RPi import GPIO
lcd = CharLCD(numbering_mode=GPIO.BOARD, cols=16, rows=2, pin_rs=37, pin_e=35, pins_data=[40, 38, 36, 32, 33, 31, 29, 23])




led= 7 #Pin nr 4.
GPIO.setup(led, GPIO.OUT) #led output

with open("[code.txt]","r") as ins: #fill in the file with the barcodes you're expecting, each code on a different line. last line ending with +++END+++
    items = []
    for line in ins:
        items.append(line[:-1])

count = 0

try:
    while True:
        code = input("Scan: ")
        if code in items:
                GPIO.output(led, 1)
                lcd.write_string("Sesam Open")
                time.sleep(1)
                lcd.clear()
                lcd.write_string("Making the mail")
                time.sleep(1)
                lcd.clear()
				
                #make the mail
                fromaddr = "[The email you want to send from]"
                toaddr = "[The Email you want to send to]"
                msg = MIMEMultipart()
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg['Subject'] = "Deilvery arrived!"
                body = "Your delivery with code: " + str(code) + " has arrived."
                msg.attach(MIMEText(body, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587) #Using gmail.com
                server.connect("smtp.gmail.com",587) #Using gmail.com
                server.ehlo()
                server.starttls()
                server.ehlo()
				
                #Next, log in to the mailserver
                server.login(fromaddr, "[Your email password]") #fill in your email pwd
                lcd.write_string("Mail ready.")
                time.sleep(1)
                lcd.clear()
                lcd.write_string("Sending...")
                time.sleep(1)
                lcd.clear()
				
                #Send the mail
                text = msg.as_string() 

                server.sendmail(fromaddr, toaddr, text)
                server.quit()
                lcd.write_string("Mail sent!")
                time.sleep(1)
                lcd.clear()
                #Close
                lcd.write_string("Waiting 5 sec to close.")
                time.sleep(1)
                lcd.clear()
                lcd.write_string("5")
                time.sleep(1)
                lcd.clear()
                lcd.write_string("4")
                time.sleep(1)
                lcd.clear()
                lcd.write_string("3")
                time.sleep(1)
                lcd.clear()
                lcd.write_string("2")
                time.sleep(1)
                lcd.clear()
                lcd.write_string("1")
                time.sleep(1)
                lcd.clear()
                lcd.write_string("closing...")
                GPIO.output(led, 0)
                time.sleep(5)
                lcd.clear()
                
                
        else:
            lcd.write_string("You shall not pass!")
            GPIO.output(led, 0)
            time.sleep(5)
            lcd.clear()
except KeyboardInterrupt:
    GPIO.cleanup()