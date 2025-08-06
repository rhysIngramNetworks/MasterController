import sys
import time

sys.path.append("/home/trains/Documents/repositories/MasterController/")
sys.path.append("C:/Users/RhysHopkins/Documents/repositories/MasterController/")

from modem.modem_controller import ModemController


modem_controller = ModemController("192.168.128.11",
                                   "ssh",
                                   "ssh",
                                   "admin",
                                   "admin")

modem_controller.login()
modem_controller.enable(0)

time.sleep(1)

modem_controller.enable(1)

time.sleep(1)

modem_controller.enable(0)