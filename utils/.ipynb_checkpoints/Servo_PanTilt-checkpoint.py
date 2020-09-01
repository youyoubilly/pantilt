from __future__ import division
import time
import Adafruit_PCA9685

class PanTilt():
    def __init__(self, channel, set_bus=0, max_angle=180, min_angle=0):
        self.set_bus = set_bus
        self.pwm = Adafruit_PCA9685.PCA9685(busnum=self.set_bus)
        self.pwm.set_pwm_freq(50)
        self.channel = channel
        self.max_angle = max_angle
        self.min_angle = min_angle
        self.angle = None
        self.reset_angle = int((max_angle + min_angle)/2)
        self.angle_unit = 10
       
    def to_angle(self, angle):
        if angle < self.min_angle or angle > self.max_angle:
            print("Invalid angle at servo channel {}".format(self.channel))
        else:
            self.angle = angle
            data=4096*((angle*180/self.max_angle*11)+500)/20000+0.5
            self.pwm.set_pwm(self.channel, 0, round(data))
           
    def reset(self):
        self.to_angle(angle=self.reset_angle)
    
    def add(self):
        if self.angle + self.angle_unit <= self.max_angle:
            self.angle = self.angle + self.angle_unit
        else:
            pass
        self.to_angle(angle=self.angle)

    def sub(self):
        if self.angle - self.angle_unit >= self.min_angle:
            self.angle=self.angle - self.angle_unit
        else:
            pass
        self.to_angle(angle=self.angle)

    def to_max(self):
        self.to_angle(angle=self.max_angle)
        
    def to_min(self):
        self.to_angle(angle=self.min_angle)