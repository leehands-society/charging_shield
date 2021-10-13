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
    
  def print_test(self):
    print("battshield test ok")
    
  def indicatebatt(self,volt):
    if volt < 3000 :
      ld_100.on()
      ld_75.on()
      ld_50.on()
      ld_25.off()
    elif volt < 3500 :
      ld_100.on()
      ld_75.on()
      ld_50.off()
      ld_25.off()
      
    elif volt < 4000 :
      ld_100.on()
      ld_75.off()
      ld_50.off()
      ld_25.off()
      
    else :
      ld_100.off()
      ld_75.off()
      ld_50.off()
      ld_25.off()
      
    
    
    

