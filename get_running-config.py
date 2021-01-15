#+--------------------------------------------------------------------------+
#|  THE FOLLOWING PYTHON FILE WAS CREATED BY JEAFFREY JAMESON BASED IN      |
#|             DAVID BOMBAL'S JOB (MY MY GRATEFULNESS TO HIM)               |
#+--------------------------------------------------------------------------+

import getpass
import sys
import telnetlib

#ENTER BETWEEN THE "" THE IP OF YOUR CISCO SWITCH OR ROUTER
HOST = " "
#ENTER BETWEEN THE "" YOUR USER TO ACCESS TO YOUR CISCO SWITCH OR ROUTER
USER = " "
#ENTER BETWEEN THE "" THE IP OF YOUR CISCO SWITCH OR ROUTER
PASSWORD = " "

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(USER + "\n")
if PASSWORD:
    tn.read_until("Password: ")
    tn.write(PASSWORD + "\n")

#THIS PART IS TO EXPAND THE LENGTH OF THE LINES IN THE TELNET CONNECTION
tn.write("config term \n")
tn.write("line vty 0 4 \n")
tn.write("login local \n")
tn.write("length 512 \n")
tn.write("transport input all \n")
tn.write("end \n")

#GET THE CONFIGURATION OF YOUR SWITCH OR ROUTER
tn.write("show startup-config \n")
tn.write("exit \n")

#CREATE THE .TXT FILE, INSERT THE NAME THAT YOU WANT BETWEEN THE "" 
f = open("ESW11.txt", "w")
f.write(tn.read_all())
f.close()

