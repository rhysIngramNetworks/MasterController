import telnetlib


class ModemController:
    def __init__(self, ip_address, user1, password1, user2, password2):
        self.ip_address = ip_address
        self.user1 = user1
        self.password1 = password1
        self.user2 = user2
        self.password2 = password2

        self.telnet = telnetlib.Telnet(ip_address)

        self.login()

    def login(self):
        # Read the first username prompt
        self.telnet.read_until(b"login:")
        self.telnet.write(self.user1.encode("utf-8") + b"\n")

        # Read the first password prompt and send the first password
        self.telnet.read_until(b"Password:")
        self.telnet.write(self.password1.encode("utf-8") + b"\n")

        # Read the second username prompt
        self.telnet.read_until(b"Username:")
        self.telnet.write(self.user2.encode("utf-8") + b"\n")

        # Read the second password prompt and send the second password
        self.telnet.read_until(b"Password:")
        self.telnet.write(self.password2.encode("utf-8") + b"\n")

    def enable(self, enable):
        pass

    def return_to_main_menu(self):
        pass

    
"""
import telnetlib
import sys
import time

# Define your Telnet connection parameters
host = "192.168.128.21"
user1 = "ssh"
password1 = "ssh"
user2 = "admin"
password2 = "admin"


# Create a Telnet object and connect to the device
tn = telnetlib.Telnet(host)
print("start")

# Read the first username prompt
tn.read_until(b"login:")
print("done")

tn.write(user1.encode("utf-8") + b"\n")
print("done")

# Read the first password prompt and send the first password
tn.read_until(b"Password:")
print("done")

tn.write(password1.encode("utf-8") + b"\n")
print("done")

# Read the second username prompt
tn.read_until(b"Username:")
print("done")

tn.write(user2.encode("utf-8") + b"\n")
print("done")

# Read the second password prompt and send the second password
tn.read_until(b"Password:")
print("done")

tn.write(password2.encode("utf-8") + b"\n")
print("done")

#Main Menu
tn.read_until(b"x. Exit")
print("#Main Menu")

tn.write(b"3\n")
print("done")

#Modules
tn.read_until(b"x. Exit")
print("#Modules")

tn.write(b"1\n")
print("done")

#TX Modules
tn.read_until(b"x. Exit")
print("#TX Modules")

tn.write(b"2\n")
print("done")

#AcmController
tn.read_until(b"x. Exit")
print("#AcmController")

tn.write(b"1\n")
print("done")

#Enter Profile Manual Value
tn.read_until(b"(y/n x=exit)")
print("#Enter Profile Manual Value")

tn.write("y\n".encode("utf-8"))
print("done")

#Set Profile Manual Value
tn.read_until(b"('x' to Exit):")

print("#Set Profile Manual Value")

#tn.write(b"Mod_Rate")
ModRate = sys.argv[1]
Mod_Rate = ModRate
mod_rate = str(Mod_Rate)
tn.write(mod_rate.encode("utf-8") + b"\n")
print("done")
print(mod_rate, Mod_Rate)

time.sleep(0.5)
# Close the Telnet session when done
tn.close()
print("closed")
"""