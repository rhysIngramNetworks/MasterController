import sys
 
sys.path.append("C:/Users/RhysHopkins/Documents/repositories/MasterController")

from modem.modem_controller import ModemController

modem = ModemController("192.168.128.11", "ssh", "ssh", "admin", "admin")
modem.set_dc_offset()
modem.logout()
modem.close()