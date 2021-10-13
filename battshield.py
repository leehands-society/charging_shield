from gpiozero import LED
from time import sleep
import smbus

class battshield :
  def __init__(self)
    self.battlevel = 0
    self.battstatus = 0
    
  def print_test(self):
    print("battshield test ok")
    
  def indicatebatt(self,volt):
    
    

