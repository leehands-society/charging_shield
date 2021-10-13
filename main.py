from gpiozero import LED
from time import sleep
import smbus
import STC3100
import battshield

stc3100 = STC3100.STC3100(0x70) # stc3100 address is '0x70'


STC3100_REG_MODE  = 0x00
STC3100_REG_ID0   = 0x18
STC3100_REG_CTRL  = 0x01   

STC3100_REG_VOLTAGE_LOW  = 0x08 
STC3100_REG_VOLTAGE_HIGH = 0x09
STC3100_REG_CURRENT_LOW  = 0x06
STC3100_REG_CURRENT_HIGH = 0x07

stc3100.startup()
battdata = []
ReadCnt = 0

while True:
    ReadCnt += 1
    if ReadCnt > 5 :
        ReadCnt = 0
    
    battdata = stc3100.readbatterydata()
    battshield.indicatebatt(battdata[1])
    
    print("Batt Curruent : ")
    print(battdata[0])
    print("Batt Volatage : ")
    print(battdata[1])
    sleep(0.25)
    
