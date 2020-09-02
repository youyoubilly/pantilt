# pantilt 舵机云台控制

这是工具包可以
1) 基于Python控制舵机；
2) 驱动基于英伟达Jetson系列板子的摄像头云台

国内小伙伴可以进入此[**Gitee传送门**](https://gitee.com/billio/servo_pan_tilt)

打开此文件[**pan_tilt_demo.ipynb**](/pan_tilt_demo.ipynb)有简单指引如何使用此工具。

### - 简单说明：
__*`channel`*__ 是舵机连接PCA9685的信号编号; \
__*`bus`*__ 可以是0或1或2; \
__*`max_angle`*__ 设置舵机最高可转的度数; \
__*`min_angle`*__ 设置舵机最低可转的度数。

__*`.to_angle`*__ 转到指定角度; \
__*`.reset`*__ 回归重置角度，默认重置角度是(max_angle+min_angle)/2; \
__*`.add`*__ 增加一个单位角度，默认单位角度为 **10** ; \
__*`.sub`*__ 减少一个单位角度; \
__*`.angle`*__ 读取当前角度位置;

赋值 __*`.reset_angle`*__ 可改变重置角度；\
赋值 __*`.angle_unit`*__ 可改变转动一个单位的角度。

### - STL 3D模型

欢迎下载我设计的此简单舵机云台，然后3D打印出来使用。

此云台可以用于Jetson Nano或树莓派。

你可以随意修改此模型用于其他目的。

当然，如果你也能分享你自己设计的云台stl模型，那就太好了！

### - 备注

有什么问题，在issues那发布出来讨论吧！

Billy Wang

BillioTech Team
比利奥



# pantilt

![](http://res.makeronsite.com/billiocar/pantilt.gif)


这是工具包可以
1) 基于Python，方便控制舵机；
2) 基于英伟达Jetson系列板子，控制一个摄像头云台。

![pan_tilt](http://res.makeronsite.com/billiocar/servo_pan_tilt.png)
![stl](http://res.makeronsite.com/billiocar/stl.png)

## 简单说明
### 1. 控制舵机
```python
from utils.servoctrl import Servo
s1 = Servo(channel=14, bus=0, max_angle=180, min_angle=0)
```
`channel` 是舵机连接PCA9685的信号编号; \
`bus` 可以是0或1或2; \
`max_angle` `min_angle` 设置舵机最高和最低可转的度数;


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

__*`.to_angle()`*__ 转到指定角度; \
__*`.reset()`*__ 回归重置角度，默认重置角度是(max_angle+min_angle)/2; \
__*`.change_reset()`*__ 括号内输入整数可改变重置角度；\
若括号`.change_reset()`空着就以当前角度更新为重置角度

__*`.add()`*__ 增加一个单位角度，默认单位角度为 **10** ; \
__*`.sub()`*__ 减少一个单位角度; \
括号内输入整数为移动单位次数。\
__*`.change_unit()`*__ 可改变转动一个单位的角度。

__*`.read()`*__ 读取当前位置角度 \
在首次启动进行下一步动作之前，此方法无法正常工作，输出None。

__*`.to_min()`*__ 移动到最大值角度 \
__*`.to_max()`*__ 移动到最小值角度 

打开jupyter notebook文件，[**servo_demo.ipynb**](/servo_demo.ipynb)试试吧！

### 2. 控制云台
控制云台两个舵机的方法与控制一个舵机相似。\
打开此jupyter notebook文件 [**pan_tilt_demo.ipynb**](/pan_tilt_demo.ipynb)试试吧！

### 3. 摄像头云台
憋大招当中……

## 前期安装
还没写好……

## STL 3D模型

欢迎下载我设计好的模型，然后3D打印出来吧。\
你可以随意根据需要修改模型。

如果你也能共享你的设计文件到项目，那就太好了！\

## 其他语言
英文文档[**GitHub - pantilt**](https://github.com/youyoubilly/pantilt) \
中文文档[**中文传送门**](/zh-chs/README.md); 国内仓库：[**Gitee传送门**](https://gitee.com/billio/servo_pan_tilt)

如果你能帮忙将此项目翻译成其他语言，那就感谢啦！\
一起为开源作出我们小小的贡献吧！

## 备注

如果你发现什么问题，发布[到这一起讨论](../..//issues)!

如果英文表达不准确，帮忙更正一下，谢谢！

Billy Wang \
BillioTech 比利奥