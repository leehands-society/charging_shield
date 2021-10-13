from gpiozero import LED
from time import sleep
import smbus
import STC3100

stc3100 = STC3100.STC3100(0x70) # stc3100 address is '0x70'


STC3100_REG_MODE  = 0x00
STC3100_REG_ID0   = 0x18
STC3100_REG_CTRL  = 0x01   

STC3100_REG_VOLTAGE_LOW  = 0x08 
STC3100_REG_VOLTAGE_HIGH = 0x09
STC3100_REG_CURRENT_LOW  = 0x06
STC3100_REG_CURRENT_HIGH = 0x07

#bus = smbus.SMBus(1) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1
#res = bus.read_byte_data(0x70,STC3100_REG_ID0)
#if res != 0x10:
#    print "fail"
#res = bus.read_byte_data(0x70,STC3100_REG_CTRL)
#print ("REG_CTR : ") 
#print res
#
#res = bus.write_byte_data(0x70,STC3100_REG_CTRL,0x02)
#print ("REG_CTR : ") 
#print res
#
#res = bus.write_byte_data(0x70,STC3100_REG_MODE,0x10)
#print ("REG_MOD : ") 
#print res

stc3100.startup()
ld_100 = LED(6)
ld_75 = LED(13)
ld_50 = LED(19)
ld_25 = LED(26)
battdata = []
ReadCnt = 0

while True:
    ReadCnt += 1
    if ReadCnt > 5 :
        ReadCnt = 0
    
    battdata = stc3100.readbatterydata()
    print("Batt Curruent : ")
    print(battdata[0])
    print("Batt Volatage : ")
    print(battdata[1])
    sleep(0.25)
    ld_100.off()
    ld_75.on()
    ld_50.off()
    ld_25.on()
    sleep(0.25)
    ld_100.on()
    ld_75.off()
    ld_50.on()
    ld_25.off()
