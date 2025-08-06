import RPi.GPIO as GPIO


class gpio():
    def __init__(self, pin_num, is_input, default=0):
        self.pin_num = pin_num
        self.is_input = is_input
        self.default = default
        self.value = default

        GPIO.setmode(GPIO.BOARD)

        if is_input:
            GPIO.setup(pin_num, GPIO.IN)
        else:
            GPIO.setup(pin_num, GPIO.OUT)
            GPIO.output(pin_num, self.default)

    def high(self):
        GPIO.output(self.pin_num, 1)
        self.value = 1

    def low(self):
        GPIO.output(self.pin_num, 0)
        self.value = 0

    def toggle(self):
        GPIO.output(self.pin_num, not self.value)

    def read(self):
        return GPIO.input(self.pin_num)
