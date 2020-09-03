# pantilt 舵机云台控制

![](http://res.makeronsite.com/billiocar/pantilt.gif)

这是工具包可以 \
1) 基于Python，控制舵机；\
2) 基于Jupyter Notebook页面插件, 控制一个两舵机摄像头云台。

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
__*`.to_min()`*__ 移动到最大值角度 \
__*`.to_max()`*__ 移动到最小值角度 

打开jupyter notebook文件，[**servo_demo.ipynb**](/servo_demo.ipynb)试试吧！

### 2. 控制云台
![](http://res.makeronsite.com/billiocar/demo2.gif)
控制云台两个舵机的方法与控制一个舵机相似。\
打开此jupyter notebook文件 [**pan_tilt_demo.ipynb**](/pan_tilt_demo.ipynb)试试吧！

### 3. 摄像头云台
![](http://res.makeronsite.com/billiocar/demo3.gif)
详细教程在此传送门：[**cam_pan_tilt_demo.ipynb**](/cam_pan_tilt_demo.ipynb)

## 前期安装
还没写好……

## STL 3D模型

![pan_tilt](http://res.makeronsite.com/billiocar/servo_pan_tilt.png)
![stl](http://res.makeronsite.com/billiocar/stl.png)

欢迎下载我设计好的模型，然后3D打印出来吧。\
你可以随意根据需要修改模型。

如果你也能共享你的设计文件到项目，那就太好了！\

## 其他语言
英文文档[**GitHub - pantilt**](https://github.com/youyoubilly/pantilt) \
中文文档[**中文传送门**](/zh-chs/README.md); 国内仓库：[**Gitee传送门**](https://gitee.com/billio/servo_pan_tilt)

如果你能帮忙将此项目翻译成其他语言，那就感谢啦！\

## 支持
此项目是非商业的，是由一个热衷于开源，希望更多人都能通过此项目共同成长，的团队发起。\
如果你觉得此项目对你十分有帮助，你可以通过[PayPal](https://www.paypal.com/paypalme/BillyYBWang)给我们团队捐赠些咖啡钱表示支持。\
有这些的支持，我们可以买新的硬件来开发更多类似的开源教育项目，并且更愿意投入更多时间到这些项目当中。

## 备注

如果你发现什么问题，发布[到这一起讨论](../..//issues)!

如果文档存在英文表达不准确，帮忙更正一下，感谢！

Billy Wang \
BillioTech 比利奥
