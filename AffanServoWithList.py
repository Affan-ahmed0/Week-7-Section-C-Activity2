#Write or paste your code here from Thonny
from machine import Pin
import time

turning = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
IN1 = Pin(5,Pin.OUT)
IN2 = Pin(14,Pin.OUT)
IN3 = Pin(15,Pin.OUT)
IN4 = Pin(18,Pin.OUT)


while True:
    for i in turning:
        IN1.value(i[0])
        IN2.value(i[1])
        IN3.value(i[2])
        IN4.value(i[3])
        time.sleep_ms(5)
