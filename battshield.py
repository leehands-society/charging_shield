###############################################
## Python Module (BATT SHIELD) from Leehands ##
## Update : 2021.10.13                       ##
## Version : Beta 0.1                        ##
## Engineer : Namhun                         ##
###############################################
from gpiozero import LED
from time import sleep
import smbus


ld_100 = LED(6)
ld_75 = LED(13)
ld_50 = LED(19)
ld_25 = LED(26)

class battshield :
  def __init__(self):
    self.battlevel = 0
    self.battstatus = 0
    self.flashingCnt = 0
    
  def print_test(self):
    print("battshield test ok")
    
  def indicatebatt(self,volt):
    if self.flashingCnt  == 1 :
      self.flashingCnt = 0
    else :
      self.flashingCnt = 1
    
    if volt < 3000 :
      ld_100.on()
      ld_75.on()
      ld_50.on()
      if self.flashingCnt = 1:      ld_25.off()
      else :                        ld_25.on()
    elif volt < 3700 :
      ld_100.on()
      ld_75.on()
      if self.flashingCnt = 1:      ld_50.off()
      else :                        ld_50.on()
      ld_25.off()      
    elif volt < 4200 :
      ld_100.on()
      if self.flashingCnt = 1:      ld_75.off()
      else :                        ld_75.on()
      ld_50.off()
      ld_25.off()
      
    else :
      if self.flashingCnt = 1:      ld_100.off()
      else :                        ld_100.on()
      ld_75.off()
      ld_50.off()
      ld_25.off()
      
    
    
    

