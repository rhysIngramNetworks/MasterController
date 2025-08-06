import smbus  # can try smbus2 or smbus

# bus_no = 1


class i2cBus:
    def __init__(self, bus_no):
        self.i2c = smbus.SMBus(bus_no)

    def write(self, address_byte, offset, data):
        self.i2c.write_i2c_block_data(address_byte, offset, data)

    def read(self, address_byte, offset, size):
        return self.i2c.read_i2c_block_data(address_byte, offset, size)
