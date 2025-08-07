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

        print("login complete")

    def enter_command(self, command):
        self.telnet.write(command.encode("utf-8")+b"\n")

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

        #FPGA Modules
        self.telnet.read_until(b"x. Exit")
        self.telnet.write(b"1\n")

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
        read = self.telnet.read_some()
        exit_phrase = "Are you sure you want to exit session (Y or N)"
        while (read.decode("utf-8").find("Exit") == -1):
            read = self.telnet.read_some()
            for i in range(len(exit_phrase))[len(exit_phrase)//2:-1]:
                if (read.decode("utf-8").find(exit_phrase[:len(exit_phrase)-i]) != -1) or \
                    (read.decode("utf-8").find(exit_phrase[i:len(exit_phrase)]) != -1):
                    self.enter_command("N")
                    return
                
            self.exit_current_menu()
            break
            
        self.return_to_main_menu()

    def exit_current_menu(self):
        self.enter_command("x")

    def logout(self):
        self.exit_current_menu()
        self.enter_command("Y")

    def close(self):
        time.sleep(0.5)
        # Close the Telnet session when done
        self.telnet.close()
