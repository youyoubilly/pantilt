[*中文文档*](/zh-chs/README.md)



# pantilt

This is a tool kit containing Python utils 
1) for driving servos,
2) for controlling camera at a two-servos pan tilt by widgets in jupyter notebook and a PS4 Joystick.

![](http://res.makeronsite.com/billiocar/pantilt.gif)

## Quick Guide
### 1. To Initiate a Servo
```python
from pantilt import Servo
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
__*`.to_min()`*__ will turn to the minimum angle. \
__*`.to_max()`*__ will turn to the maximum angle.

You can open a jupyter notebook file, [**servo_demo.ipynb**](/servo_demo.ipynb), to have a try on this tool kit.

### 2. To Initiate a Pan Tilt

![](http://res.makeronsite.com/billiocar/demo2.gif)

Its methods to control two servos at a pan tilt is similar to control a servo, here is a jupyter notebook file [**pan_tilt_demo.ipynb**](/pan_tilt_demo.ipynb)

### 3. Camera Pan Tilt

![](http://res.makeronsite.com/billiocar/demo3.gif)

Walkthrough is here [**cam_pan_tilt_demo.ipynb**](/cam_pan_tilt_demo.ipynb)

## Install

1. Clone the project, please rememeber to clone with parameter —recurse-submodules, because pantilt project referene another submodule [bcam](https://github.com/youyoubilly/bcam/).

```
git clone --recurse-submodules  https://github.com/youyoubilly/pantilt.git
```

2. Install pantilt



## STL 3D Model

![pan_tilt](http://res.makeronsite.com/billiocar/servo_pan_tilt.png)
![stl](http://res.makeronsite.com/billiocar/stl.png)

You are welcome to download the stl file I designed for this simple pan tilt of CSI camera, and 3D print it out. \
You may adjust the stl model for different use.

## Other Languages
English document is available here: [**GitHub - pantilt**](https://github.com/youyoubilly/pantilt) \
Chinese document is available here: [**中文传送门**](/zh-chs/README.md); 国内仓库：[**Gitee传送门**](https://gitee.com/billio/servo_pan_tilt)

It would be **appreciated** if you can contribute to write this document in other languages!

## Donate

This project is developed on a non-commercial basis by Open Source enthusiasts. \
If you find __*pantilt*__ useful, you can support the lead developer by donating a few dollars via [PayPal](https://www.paypal.com/paypalme/BillyYBWang).
With this money, we will be able to buy new hardware to test and do more such project for open source and for free education, and generally devote significantly more time to these projects.

## Notes

If you find an issue, please [let us know](../..//issues)!

Sorry that I may have some typos or inaccurate expression in English, help me to correct them if you found one! Big Thanks!

Enjoy!

# Useful Links
- Project: [billiocar](https://github.com/youyoubilly/billiocar) \
Let's learn and play an robotic car with AI technology

- Project: [pantilt](https://github.com/youyoubilly/pantilt) \
This is a tool kit for controlling two servos at a pan tilt in jupyter notebook.

- Project: [bcam](https://github.com/youyoubilly/bcam) \
bcam is an easy to use Python camera interface for NVIDIA Jetson and Raspberry Pi.

Billy Wang \
BillioTech Team
