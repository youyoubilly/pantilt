from __future__ import division
import time
import Adafruit_PCA9685

class Servo():
    def __init__(self, channel, bus=0, max_angle=180, min_angle=0):
        self.bus = bus
        self.pwm = Adafruit_PCA9685.PCA9685(busnum=self.bus)
        self.pwm.set_pwm_freq(50)
        self.channel = channel
        self.max_angle = max_angle
        self.min_angle = min_angle
        self.angle = int((max_angle + min_angle)/2)
        self.reset_angle = int((max_angle + min_angle)/2)
        self.unit = 2
       
    def to_angle(self, angle):
        if angle < self.min_angle:
            self.angle = self.min_angle
        elif angle > self.max_angle:
            self.angle = self.max_angle
        else:
            self.angle = angle
        data=4096*((angle*180/self.max_angle*11)+500)/20000+0.5
        self.pwm.set_pwm(self.channel, 0, round(data))
           
    def reset(self):
        self.to_angle(angle=self.reset_angle)
    
    def add(self, t=1):
        for i in range(0, t):
            if self.angle + self.unit <= self.max_angle:
                self.angle = self.angle + self.unit
            else:
                self.angle=self.max_angle
            self.to_angle(angle=self.angle)

    def sub(self, t=1):
        for i in range(0, t):
            if self.angle - self.unit >= self.min_angle:
                self.angle=self.angle - self.unit
            else:
                self.angle=self.min_angle
            self.to_angle(angle=self.angle)

    def to_max(self):
        self.to_angle(angle=self.max_angle)
        
    def to_min(self):
        self.to_angle(angle=self.min_angle)
        
    def change_unit(self, unit):
        self.unit = unit
        
    def change_reset(self, reset=None):
        self.reset_angle = self.angle if reset==None else reset
        
    def read(self):
        return self.angle
        
class PanTilt():
    def __init__(self, bus=0):
        self.bus = bus
        
    def add_rl_servo(self, channel, max_angle=180, min_angle=0):
        self.rl = Servo(channel=channel, bus=self.bus, max_angle=max_angle, min_angle=min_angle)
        
    def add_ud_servo(self, channel, max_angle=180, min_angle=0):
        self.ud = Servo(channel=channel, bus=self.bus, max_angle=max_angle, min_angle=min_angle)
        
    def to_angle(self, rl=None, ud=None):
        self._nothing if rl==None else self.rl.to_angle(rl)
        self._nothing if ud==None else self.ud.to_angle(ud)
        
    def reset(self):
        self.rl.reset()
        self.ud.reset()
            
    def go_left(self, t=1):
        self.rl.add(t)
        
    def go_right(self, t=1):
        self.rl.sub(t)

    def go_up(self, t=1):
        self.ud.sub(t)
        
    def go_down(self, t=1):
        self.ud.add(t)
        
    def go_up_left(self, t=1):
        self.ud.sub(t)
        self.rl.add(t)
        
    def go_up_right(self, t=1):
        self.ud.sub(t)
        self.rl.sub(t)
        
    def go_down_left(self, t=1):
        self.ud.add(t)
        self.rl.add(t)
        
    def go_down_right(self, t=1):
        self.ud.add(t)
        self.rl.sub(t)
        
    def far_left(self):
        self.rl.to_max()
        self.ud.to_angle(int((self.ud.max_angle + self.ud.min_angle)/2))

    def far_right(self):
        self.rl.to_min()
        self.ud.to_angle(int((self.ud.max_angle + self.ud.min_angle)/2))

    def far_up(self):
        self.ud.to_min()
        self.rl.to_angle(int((self.rl.max_angle + self.rl.min_angle)/2))
        
    def far_down(self):
        self.ud.to_max()
        self.rl.to_angle(int((self.rl.max_angle + self.rl.min_angle)/2))

    def upper_left(self):
        self.ud.to_min()
        self.rl.to_max()

    def upper_right(self):
        self.ud.to_min()
        self.rl.to_min()

    def lower_left(self):
        self.ud.to_max()
        self.rl.to_max()

    def lower_right(self):
        self.ud.to_max()
        self.rl.to_min()
        
    def change_unit(self, rl, ud):
        self.rl.unit = rl
        self.ud.unit = ud
        
    def change_reset(self, rl=None, ud=None):
        self.rl.change_reset(reset=rl)
        self.ud.change_reset(reset=ud)
    
    def read(self):
        return self.rl.angle, self.ud.angle

    def _nothing(self):
        pass