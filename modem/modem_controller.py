import telnetlib
import time


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

    def set_acm(self, acm_level):
        #Main Menu
        self.telnet.read_until(b"x. Exit")
        self.telnet.write(b"3\n")

        #Modules
        self.telnet.read_until(b"x. Exit")
        self.telnet.write(b"1\n")

        #TX Modules
        self.telnet.read_until(b"x. Exit")
        self.telnet.write(b"2\n")

        #AcmController
        self.telnet.read_until(b"x. Exit")
        self.telnet.write(b"1\n")

        #Enter Profile Manual Value
        self.telnet.read_until(b"(y/n x=exit)")
        self.telnet.write("y\n".encode("utf-8"))

        #Set Profile Manual Value
        self.telnet.read_until(b"('x' to Exit):")

        mod_rate = str(acm_level)
        self.telnet.write(mod_rate.encode("utf-8") + b"\n")

        self.return_to_main_menu()

    def set_dc_offset(self):
        #Main Menu
        self.telnet.read_until(b"x. Exit")
        self.telnet.write(b"3\n")

        #Modules
        self.telnet.read_until(b"x. Exit")
        self.telnet.write(b"1\n")

        #TX Modules
        self.telnet.read_until(b"x. Exit")
        self.telnet.write(b"2\n")

        #Digital Tx
        self.telnet.read_until(b"x. Exit")
        self.telnet.write(b"6\n")

        #Configure DC Offset
        self.telnet.read_until(b"x. Exit")
        self.telnet.write(b"4\n")

        #Enter DC Offsets
        self.telnet.read_until(b"(y/n x=exit)")
        self.telnet.write("n\n".encode("utf-8"))

        #Set DC Offsets
        for _ in range(3):
            self.telnet.read_until(b"('x' to Exit):")
            mod_rate = str(0)
            self.telnet.write(mod_rate.encode("utf-8") + b"\n")

        #Confirm DC Offsets
        self.telnet.read_until(b"(y/n x=exit)")
        self.telnet.write("y\n".encode("utf-8"))

        self.return_to_main_menu()

    def return_to_main_menu(self):
        self.telnet.read_until("Exit")
        return

    def close(self):
        time.sleep(0.5)
        # Close the Telnet session when done
        self.telnet.close()

    
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