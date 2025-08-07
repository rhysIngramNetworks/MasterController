import sys

sys.path.append("/home/trains/Documents/repositories/MasterController/")

from communications.gpio import gpio

    
busCA = gpio(5,0,0)
busCB = gpio(3,0,0)

busDA = gpio(29,0,0)
busDB = gpio(7,0,0)

red1 = gpio(36,0,0)
red2 = gpio(37,0,0)
red3 = gpio(21,0,0)

yellow1 = gpio(19,0,0)
yellow2 = gpio(23,0,0)
yellow3 = gpio(32,0,0)

blue1 = gpio(33,0,0)
blue2 = gpio(8,0,0)
blue3 = gpio(10,0,0)

gpios = [red1, red2, red3, yellow1, yellow2, yellow3, blue1, blue2, blue3, busCA, busCB, busDA, busDB]


def main():
    with open("/home/trains/Documents/repositories/MasterController/configs/dcOffsetCalibrations.txt") as f:
        for line in f:
        
            items = line.replace("\n","").split(",")
            
            if (len(items)>1):
            
                for io in gpios:
                    if io.pin_num == int(items[0]):
                        io.set(int(items[1]))

main()
