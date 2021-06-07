#!/usr/bin/env python3
import smtplib, ssl
import sys
port = 465

context = ssl.create_default_context()
sender_email = "weatheralertpi@gmail.com"
receiver_email = "8564122706@messaging.sprintpcs.com"

#message = "\n" + sys.argv[2]

message = "\n" + "The " + sys.argv[1] + " has issued a " + sys.argv[2] + " until " + sys.argv[3] + "."

#print (message)

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("weatheralertpi@gmail.com", "BMW330ci!")
    server.sendmail(sender_email, receiver_email, message)
