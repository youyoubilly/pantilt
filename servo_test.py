# -*- coding: utf-8 -*-

from __future__ import division
import time
import Adafruit_PCA9685

print('-----------  Test for Servo  -----------') 
print('(Press Ctrl-C to quit...)')

set_bus = int(input('Input BUS number:'))

# Initialise the PCA9685 using the default address (0x40).
pwm = Adafruit_PCA9685.PCA9685(busnum=set_bus)
# Alternatively specify a different address and/or bus:
# for example, pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

def set_servo_angle(channel,angle):
    date=4096*((angle*11)+500)/20000 + 0.5
    pwm.set_pwm(channel,0,int(date))

pwm.set_pwm_freq(50)

while True:
    # Move servo on channel O between extremes.
    set_channel = int(input('Input channel:'))
    set_angle = 0
    print('(Press Input "-1" back to change channel)')
    while set_angle != -1:
        set_angle = int(input('Input angle (0~180):'))
        if set_angle >= 0 and set_angle <= 180:
            set_servo_angle(set_channel, set_angle)
            print('channel:', set_channel, '  pwm freq:', 4096*((set_angle*11)+500)/20000 + 0.5)