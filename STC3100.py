###########################################
## Python Module (STC3100) from Leehands ##
## Update : 2021.10.10                   ##
## Version : Beta 0.1                    ##
## Engineer : Namhun                     ##
###########################################
import smbus

STC3100_REG_MODE               = 0x00 # Mode Register
STC3100_REG_CTRL               = 0x01 # Control and Status Register   
STC3100_REG_CHARGE_LOW         = 0x02 # Gas Gauge Charge Data Bits 0-7
STC3100_REG_CHARGE_HIGH        = 0x03 # Gas Gauge Charge Data Bits 8-15 
STC3100_REG_COUNTER_LOW        = 0x04 # Number of Conversion Bits 0-7
STC3100_REG_COUNTER_HIGH       = 0x05 # Number of Conversion Bits 8-15
STC3100_REG_CURRENT_LOW        = 0x06 # Battery Current Value Bits 0-7
STC3100_REG_CURRENT_HIGH       = 0x07 # Battery Current Value Bits 8-15
STC3100_REG_VOLTAGE_LOW        = 0x08 # Battery Voltage Value Bits 0-7
STC3100_REG_VOLTAGE_HIGH       = 0x09 # Battery Voltage Value Bits 8-15
STC3100_REG_TEMPERATURE_LOW    = 0x0A # Temperature Values Bits 0-7) 
STC3100_REG_TEMPERATURE_HIGH   = 0x0B # Temperature Values Bits 8-15)

STC3100_REG_ID0                = 0x18 # Part Type ID 10h  
STC3100_REG_ID1                = 0x19 # Unique Part ID Bits 0-7  
STC3100_REG_ID2                = 0x1A # Unique Part ID Bits 8-15  
STC3100_REG_ID3                = 0x1B # Unique Part ID Bits 16-23  
STC3100_REG_ID4                = 0x1C # Unique Part ID Bits 24-31  
STC3100_REG_ID5                = 0x1D # Unique Part ID Bits 32-39  
STC3100_REG_ID6                = 0x1E # Unique Part ID Bits 40-47  
STC3100_REG_ID7                = 0x1F # Device ID CRC

STC3100_RAM_SIZE               = 32  # Total RAM register of STC3100

STC3100_REG_RAM0               = 0x20  
STC3100_REG_RAM2               = 0x22
STC3100_REG_RAM4               = 0x24
STC3100_REG_RAM6               = 0x26
STC3100_REG_RAM8               = 0x28  
STC3100_REG_RAM12              = 0x2C  
STC3100_REG_RAM14              = 0x2E  
STC3100_REG_RAM16              = 0x30  
STC3100_REG_RAM18              = 0x32 
STC3100_REG_RAM20              = 0x34 
STC3100_REG_RAM22              = 0x36 
STC3100_REG_RAM24              = 0x38 
STC3100_REG_RAM26              = 0x3A 
STC3100_REG_RAM28              = 0x3C 
STC3100_REG_RAM30              = 0x3E 

STC3100_OK  = 0

##############################################################################
SENSERESISTOR  =  33    # sense resistor value in milliOhms (10min, 100max)
                        #TO BE DEFINED ACCORDING TO HARDWARE IMPLEMENTATION
##############################################################################

CurrentFactor     = (48210/SENSERESISTOR)   # LSB=11.77uV/R= ~48210/R/4096 - convert to mA
ChargeCountFactor = (27443/SENSERESISTOR)   # LSB=6.7uVh/R ~27443/R/4096 - converter to mAh
VoltageFactor     = 9994                    # LSB=2.44mV ~9994/4096 - convert to mV
TemperatureFactor = 5120                    # LSB=0.125°C ~5120/4096 - convert to 0.1°C


class STC3100:
  def __init__(self,addr):
    self.addr = addr
    self.bus = smbus.SMBus(1) # 0 = /dev/i2c-0 , 1 = /dev/i2c-1
  def print_test(self):
    print("STC3100 test ok")
    
  def startup(self):
    #first, check the presence of the STC3100 by reading first byte of dev. ID
    s32_res = self.readbyte(STC3100_REG_ID0)
    if s32_res!= 0x10:
      return (-1)
    
    #read the REG_CTRL to reset the GG_EOC and VTM_EOC bits
    self.readbyte(STC3100_REG_CTRL)

    #write 0x02 into the REG_CTRL to reset the accumulator and counter and clear the PORDET bit,
    s32_res = self.writebyte(STC3100_REG_CTRL, 0x02)
    if (s32_res!= STC3100_OK) :
      return (s32_res)

    #then 0x10 into the REG_MODE register to start the STC3100 in 14-bit resolution mode.
    s32_res = self.writebyte(STC3100_REG_MODE, 0x10)
    if (s32_res!= STC3100_OK) :
      return (s32_res)

    return (STC3100_OK)
  def powerdown(self):
    s32_res = self.writebyte(STC3100_REG_MODE , 0)
    if(s32_res != STC3100_OK):
      return s32_res
  def readbatterydata(self):
    pu8_data[0] = self.readbyte(0)
    pu8_data[1] = self.readbyte(1)
    pu8_data[2] = self.readbyte(2)
    pu8_data[3] = self.readbyte(3)
    pu8_data[4] = self.readbyte(4)
    pu8_data[5] = self.readbyte(5)
    pu8_data[6] = self.readbyte(6)
    pu8_data[7] = self.readbyte(7)
    pu8_data[8] = self.readbyte(8)
    pu8_data[9] = self.readbyte(9)
    pu8_data[10] = self.readbyte(10)
    pu8_data[11] = self.readbyte(11)
    #charge count
    s16_value = pu8_data[3]
    s16_value = (s16_value<<8) + pu8_data[2]
    s16_BattChargeCount = self.conv(s16_value,ChargeCountFactor) # result in mAh
    
  def conv(self,value,factor):
    return( ( (s32) s16_value * u16_factor ) >> 12 )
    
    
  def writebyte(self,cmd,data):
    res = self.bus.write_byte_data(self.addr,cmd,data)
    if res == STC3100_OK:
      res = 0
    else:
      res = -1
    return res
    
  def readbyte(self,cmd):
    res = self.bus.read_byte_data(self.addr,cmd)
    return res
    
  def print_test(self):
    print("STC3100 is ok")
