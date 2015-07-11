#!/usr/bin/env python

# Follow the warnings thrown by IMAP to enable gmail settings.

from imapclient import IMAPClient
import time
import sys
 
import RPi.GPIO as GPIO
 
DEBUG = True
 
HOSTNAME = 'imap.gmail.com'
USERNAME = 'username'
PASSWORD = 'passw'
MAILBOX = 'Inbox'
 
MAIL_CHECK_FREQ = 60 # check mail every 60 seconds
 
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GREEN_LED = 23
RED_LED = 18
GPIO.setup(GREEN_LED, GPIO.OUT)
GPIO.setup(RED_LED, GPIO.OUT)

# testing both leds

GPIO.output(GREEN_LED, True)
GPIO.output(RED_LED, True)


time.sleep(10)

GPIO.output(GREEN_LED, False)
GPIO.output(RED_LED, False)

oldmails = sys.maxint

def loop():
    global oldmails

    server = IMAPClient(HOSTNAME, use_uid=True, ssl=True)
    server.login(USERNAME, PASSWORD)
 
    if DEBUG:
        print('Logging in as ' + USERNAME)
        select_info = server.select_folder(MAILBOX)
        print('%d messages in INBOX' % select_info['EXISTS'])
 
    folder_status = server.folder_status(MAILBOX, 'UNSEEN')
    newmails = int(folder_status['UNSEEN'])


    if DEBUG:
        print "You have", newmails, "new emails!"
 
    if newmails > oldmails:
        GPIO.output(GREEN_LED, True)
        GPIO.output(RED_LED, False)
    else:
        GPIO.output(GREEN_LED, False)
        GPIO.output(RED_LED, True)
 
    time.sleep(MAIL_CHECK_FREQ)
    oldmails = newmails
 
if __name__ == '__main__':
    try:
        print 'Press Ctrl-C to quit.'
        while True:
            loop()
    finally:
        GPIO.cleanup()

