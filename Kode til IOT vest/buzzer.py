from machine import Pin
from time import sleep

buzzer = Pin(32, Pin.OUT)

def set_buzzer():
   
    buzzer.value(1)
#     sleep(2)
#     buzzer.value(0)
    
def clear_buzzer():
    buzzer.value(0)

# buzzer.set_buzzer()