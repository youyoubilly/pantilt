# pantilt

![](http://res.makeronsite.com/billiocar/pantilt.gif)

This is a tool kit containing Python utils 
1) for controlling servos, and 
2) for driving camera based on Nvidia Jetson boards at a two-servos pan tilt.

![pan_tilt](http://res.makeronsite.com/billiocar/servo_pan_tilt.png)
![stl](http://res.makeronsite.com/billiocar/stl.png)

## Quick Guide
### 1. To Initiate a Servo
```python
from utils.servoctrl import Servo
s1 = Servo(channel=14, bus=0, max_angle=180, min_angle=0)
```
`channel` is number that servo has connected to PCA9685 board; \
`bus` can be 0 or 1 or even 2; \
`max_angle` `min_angle` is upper and lower limit we set for the servo.


```python
s1.to_angle(45)
s1.reset()
s1.change_reset(0)
s1.add()
s1.sub(3)
s1.read()
s1.change_unit(30)
s1.to_min()
s1.to_max()
```

__*`.to_angle()`*__ will turn to a angle; \
__*`.reset()`*__ will turn servo back to the default angle, which is (max_angle+min_angle)/2 as default; \
__*`.change_reset()`*__ This will change the default reset angle to input number. \
Leaving bracket blank as `.change_reset()` will apply the current angle.

__*`.add()`*__ changes the servo by adding one unit of angle, which is 10 degree as default. \
__*`.sub()`*__ changes the servo by subtracting one unit of angle; \
An integer in its bracket means how many unit it will act on. \
__*`.change_unit()`*__ will change how many degree it turn for one unit.

__*`.read()`*__ can read the current angle of the servo. \
This function won't work properly and return *None* at the initial status until it has made one move. \

__*`.to_min()`*__ will turn to the minimum angle. \
__*`.to_max()`*__ will turn to the maximum angle.

You can open a jupyter notebook file, [**servo_demo.ipynb**](/servo_demo.ipynb), to have a try on this tool kit.

### 2. To Initiate a Pan Tilt
Methods to control two servos at a pan tilt is similar to control a servo. \
Have a try here: [**pan_tilt_demo.ipynb**](/pan_tilt_demo.ipynb)

### 3. Camera Pan Tilt
This is a work still in progress...

## Install
This is a work still in progress...

## STL 3D Model

You are welcome to download the stl file I designed for the simple pan tilt of CSI camera, and 3D print it out. \
It can used for Jetson nao or Raspberry Pi. \
You may adjust the stl model for different use.

If you have other stl designs of pan tilt for sharing, it would be appreciated! \
I will add it to stl folder as well.

## Other Languages
English document is available here: [**GitHub - pantilt**](https://github.com/youyoubilly/pantilt) \
Chinese document is available here: [**中文文档传送门**](/zh-chs/README.md) 国内仓库：[**Gitee传送门**](https://gitee.com/billio/servo_pan_tilt)

It would be **appreciated** if you can contribute to write this document in other languages!

## Note

If you find an issue, please [let us know](../..//issues)!

Sorry that I may have some typos or inaccurate expression in English, help me to correct them if you found one! \
Big Thanks!

Enjoy!

Billy Wang \
BillioTech Team

