from __future__ import division
import time
import Adafruit_PCA9685

class Servo():
    def __init__(self, channel, bus=1, lower=0, upper=180, spec=180):
        self.pwm = Adafruit_PCA9685.PCA9685(address=0x40, busnum=bus)
        self.pwm.set_pwm_freq(50)
        self.channel = channel
        self.upper, self.lower = upper, lower
        self.spec = spec #max_angleium angle as its Specification
        self.mid_angle = int((self.upper + self.lower)/2)
        self.angle = self.mid_angle #Set the middle value as initial angle
        self.reset_angle = self.mid_angle #Set the middle value as reset angle
        self.unit = 2
        self.to_angle(self.reset_angle)
       
    def to_angle(self, angle):
        if angle < self.lower:
            self.angle = self.lower
        elif angle > self.upper:
            self.angle = self.upper
        else:
            self.angle = angle
        freq=4096*((self.angle/self.spec*180*11)+500)/20000+0.5
        self.pwm.set_pwm(self.channel, 0, round(freq))
           
    def reset(self):
        self.to_angle(angle=self.reset_angle)
    
    def add(self, t=1):
        for i in range(0, t):
            if self.angle + self.unit <= self.upper:
                self.angle = self.angle + self.unit
            else:
                self.angle=self.upper
            self.to_angle(angle=self.angle)

    def sub(self, t=1):
        for i in range(0, t):
            if self.angle - self.unit >= self.lower:
                self.angle=self.angle - self.unit
            else:
                self.angle=self.lower
            self.to_angle(angle=self.angle)

    def to_max(self):
        self.to_angle(angle=self.upper)
        
    def to_min(self):
        self.to_angle(angle=self.lower)
        
    def change_unit(self, unit):
        self.unit = unit
        
    def change_reset(self, reset=None):
        self.reset_angle = self.angle if reset==None else reset
        
    def read(self):
        return self.angle
        
class ServoGroup():
    def __init__(self, rl_ch, ud_ch, bus=1):
        self.bus = bus
        self.rl = Servo(channel=rl_ch, bus=bus, lower=0, upper=180, spec=180)
        self.ud = Servo(channel=ud_ch, bus=bus, lower=0, upper=180, spec=180)

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
        self.ud.to_angle(self.ud.mid_angle)

    def far_right(self):
        self.rl.to_min()
        self.ud.to_angle(self.ud.mid_angle)

    def far_up(self):
        self.ud.to_min()
        self.rl.to_angle(self.rl.mid_angle)
        
    def far_down(self):
        self.ud.to_max()
        self.rl.to_angle(self.rl.mid_angle)

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