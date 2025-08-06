import spidev


class spiBus:
    def __init__(self, bus, device, mode, clk_hz, spi=False):
        if spi:
            self.spi = spi
            self.spi.cshigh = False
            return
        self.mode = mode
        self.spi = spidev.SpiDev()
        self.spi.open(bus, device)  # Use bus 0, device 0
        self.spi.mode = mode  # SPI mode 0b01 (CPOL=0, CPHA=1)
        self.clk_hz = clk_hz
        self.spi.max_speed_hz = clk_hz  # Set the clock speed (10 MHz)
        self.spi.cshigh = False

    def send(self, data_int_list):
        return self.spi.xfer(data_int_list)

    def writebytes(self, data_list):
        self.spi.writebytes(data_list)

    def set_fq(self, fq_hz):
        self.spi.max_speed_hz = fq_hz

    def set_clk_falling(self):
        self.mode = self.mode | 0b01
        self.spi.mode = self.mode

    def set_clk_rising(self):
        self.mode = self.mode & 0b10
        self.spi.mode = self.mode
        
    def set_mode(self, mode):
        self.mode = mode
        self.spi.mode = mode
