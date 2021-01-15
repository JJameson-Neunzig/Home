import getpass
import sys
import telnetlib

HOST = "10.5.15.1"
#USER = raw_input("Enter your telnet username: ")
USER = "jeaffrey"
#PASSWORD = getpass.getpass()
PASSWORD = "passcisco"

tn = telnetlib.Telnet(HOST)

tn.read_until("Username: ")
tn.write(USER + "\n")
if PASSWORD:
    tn.read_until("Password: ")
    tn.write(PASSWORD + "\n")

#tn.write("show runn \n")
#tn.write(" \n")
#tn.write(" \n")
#tn.write("int loop 0\n")
#tn.write("ip address 1.1.1.1 255.255.255.255\n")
#tn.write("int loop 1\n")
#tn.write("ip address 2.2.2.2 255.255.255.255\n")
#tn.write("router ospf 1\n")
#tn.write("network 0.0.0.0 255.255.255.255 area 0\n")
tn.write("show clock \n")
tn.write("exit \n")

#print tn.read_all()

f = open("ESW11.txt", "a")

#f = open("ESW11.txt", "w")
f.write(tn.read_all())
f.close()

