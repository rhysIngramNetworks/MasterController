from gpiozero import Button
from gpiozero import LED

pinNumber2GpioNumberRpi5 = {
    1: -1,
    2: -1,
    3: 2,
    4: -1,
    5: 3,
    6: -1,
    7: 4,
    8: 14,
    9: -1,
    10: 15,
    11: 17,
    12: 18,
    13: 27,
    14: -1,
    15: 22,
    16: 23,
    17: -1,
    18: 24,
    19: 10,
    20: -1,
    21: 9,
    22: 25,
    23: 11,
    24: 8,
    25: -1,
    26: 7,
    27: 0,
    28: 1,
    29: 5,
    30: -1,
    31: 6,
    32: 12,
    33: 13,
    34: -1,
    35: 19,
    36: 16,
    37: 26,
    38: 20,
    39: -1,
    40: 21
}


class gpio():
    def __init__(self, pin_num, is_input, default=0):
        self.pin_num = pinNumber2GpioNumberRpi5[pin_num]
        if self.pin_num < 0:
            print("Error, pin number is either 3.3v, 5v or ground")
        self.default = default
        self.value = default
        self.gp = None
        if is_input:
            self.gp = Button(self.pin_num)
        else:
            self.gp = LED(self.pin_num)
            if default:
                self.high()

    def high(self):
        self.gp.on()
        self.value = 1

    def low(self):
        self.gp.off()
        self.value = 0

    def toggle(self):
        self.gp.toggle()
        self.value = not self.value

    def read(self):
        return self.gp.value()
