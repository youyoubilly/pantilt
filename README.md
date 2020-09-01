# Servo_Pan_Tilt

![](http://res.makeronsite.com/billiocar/pantilt.gif)

This is a tool kit for controlling two servos at a simple pan tilt or more servos if you like.

![pan_tilt](http://res.makeronsite.com/billiocar/servo_pan_tilt.png)
![stl](http://res.makeronsite.com/billiocar/stl.png)

### Quick Guide
```python
from utils.ServoControl import ServoCtrl
s1 = ServoCtrl(channel=14, set_bus=0, max_angle=180, min_angle=0)
```

`channel` is number that servo has connected to PCA9685 board; \
`set_bus` can be 0 or 1 or even 2; \
`max_angle` is upper limit we set for servo; \
`min_angle` is lower limit we set for servo. \

```python
s1.to_angle(45)
s1.reset()
s1.reset_angle = 0
s1.reset()
s1.add()
s1.sub()
s1.angle
s1.angle_unit = 30
```

`.to_angle` will turn to a angle;
`.reset` will turn servo back to the default angle, which is (max_angle+min_angle)/2 as default;
`.add` changes the servo by adding one unit of angle by this call, which is **10** degree as default;
`.sub` changes the servo by subtracting one unit of angle;
`.angle` can read the current angle;

An assignment to `.reset_angle` will reset the default angle for the servo reseting;
An assignment to `.angle_unit` will change one unit of changing angle degree.

You can open a jupyter notebook file, [**pan_tilt_demo.ipynb**](/pan_tilt_demo.ipynb), to have a try on this tool kit.

### STL 3D Model

You are welcome to download the stl file I designed for the simple pan tilt of CSI camera, and 3D print it out.

It can used for Jetson nao or Raspberry Pi.

You may adjust the stl model for different use.

It would be **appreciated** if you can share your own stl design of pan tilt as well if you have one! 

### Note

If you find an issue, please [let us know](../..//issues)!

Sorry that I may have some typos in this this repo.

Enjoy!

Billy Wang

BillioTech

----------------

# 舵机云台控制

这是可以控制两舵机云台的小工具。

国内小伙伴可以进入此[**传送门**](https://gitee.com/billio/servo_pan_tilt)

打开此文件[**pan_tilt_demo.ipynb**](/pan_tilt_demo.ipynb)有简单指引如何使用此工具。

### 简单说明：
`channel` 是舵机连接PCA9685的信号编号; \
`set_bus` 可以是0或1或2; \
`max_angle` 设置舵机最高可转的度数; \
`min_angle` 设置舵机最低可转的度数. \

`.to_angle` 转到指定角度;
`.reset` 回归重置角度，默认重置角度是(max_angle+min_angle)/2;
`.add` 增加一个单位角度，默认单位角度为 **10** ;
`.sub` 减少一个单位角度;
`.angle` 读取当前角度位置;

赋值`.reset_angle`可改变重置角度；
赋值`.angle_unit`可改变转动一个单位的角度。

### STL 3D模型

欢迎下载我设计的此简单舵机云台，然后3D打印出来使用。

此云台可以用于Jetson Nano或树莓派。

你可以随意修改此模型用于其他目的。

当然，如果你也能分享你自己设计的云台stl模型，那就太好了！

### 备注

有什么问题，在issues那发布出来讨论吧！

Billy Wang

BillioTech 比利奥科技

