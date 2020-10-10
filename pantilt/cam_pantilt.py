import traitlets
import ipywidgets.widgets as widgets
import time
import numpy as np

from bcam.bcam import Camera, frame_dp, bgr8_to_jpeg
from pantilt.pantilt.pantilt import PanTilt
import ipywidgets.widgets as widgets
from ipywidgets import Button, HBox, VBox
import os

class CamPanTilt():
    def __init__(self):
        self.pt = PanTilt(bus=0)
        self.pt.add_rl_servo(channel=14, max_angle=180, min_angle=0)
        self.pt.add_ud_servo(channel=15, max_angle=180, min_angle=0)
        self.width_dp = 320
        self.height_dp = 240
        self.image_widget = widgets.Image(format='jpeg', width=self.width_dp, height=self.height_dp)
        self.snap_count = widgets.IntText(description='count:', layout=widgets.Layout(width='140px'), value=0)
        self.rl_textbox = widgets.IntText(layout=widgets.Layout(width='148px'), value=self.pt.read()[0], description='rl:')
        self.ud_textbox = widgets.IntText(layout=widgets.Layout(width='148px'), value=self.pt.read()[1], description='ud:')
        self.rl_slider = widgets.FloatSlider(min=-1, max=1, value=0, step=0.02, description='rl')
        self.ud_slider = widgets.FloatSlider(min=-1, max=1, value=0, step=0.02, description='ud')
        self.snap_dir = 'snap'
        self.camera_link = None
        self.controller = None
        self.press_count = 0
        
    def cam(self, width_cap=800, height_cap=600, fps_cap=2, flip=2):
        camera = Camera(width=width_cap, height=height_cap, fps=fps_cap, is_usb=False, flip=flip)
        self.camera_link = traitlets.dlink((camera, 'value'), (self.image_widget, 'value'), transform=frame_dp)
        return self.image_widget

    def _rl_val(self, val):
        return int((val * (self.pt.rl.max_angle - self.pt.rl.min_angle) + self.pt.rl.max_angle + self.pt.rl.min_angle) / 2)
    
    def _ud_val(self, val):
        return int((val * (self.pt.rl.max_angle - self.pt.rl.min_angle) + self.pt.rl.max_angle + self.pt.rl.min_angle) / 2)

    def _rl_move1(self, change):
        val = change['new']
        self.pt.to_angle(rl=self._rl_val(val=val))

    def _ud_move1(self, change):
        val = change['new']
        self.pt.to_angle(ud=self._ud_val(val=val))
        
    def _rl_move2(self, change):
        val = change['new']
        self.pt.to_angle(rl=val)
        
    def _ud_move2(self, change):
        val = change['new']
        self.pt.to_angle(ud=val)
        
    def _sider_to_left(self, val):
        return self.pt.rl.max_angle * val - (val - 1) * (self.pt.rl.max_angle - self.pt.rl.min_angle) / 2
    
    def _sider_to_right(self, val):
        return self.pt.rl.min_angle * val - (val - 1) * (self.pt.rl.max_angle - self.pt.rl.min_angle) / 2
    
    def _sider_left_cam(self, change):
        val = change['new']
        if self.controller.buttons[7].value == 0:
            self.pt.to_angle(rl=self._sider_to_left(val=val))

    def _sider_right_cam(self, change):
        val = change['new']
        if self.controller.buttons[6].value == 0:
            self.pt.to_angle(rl=self._sider_to_right(val=val))
    
    def pos_box(self):
        self.rl_textbox.observe(self._rl_move2, names=['value'])
        self.ud_textbox.observe(self._ud_move2, names=['value'])
        return HBox([self.rl_textbox, self.ud_textbox])
        
    def sliders(self):
        self.rl_slider.observe(self._rl_move1, names=['value'])
        self.ud_slider.observe(self._ud_move1, names=['value'])
        return VBox([self.rl_slider, self.ud_slider])

    def panel_dir(self):
        button_layout = widgets.Layout(width='100px', height='80px', align_self='center')

        step_move = ['↖', '↑', '↗', '←', 'reset', '→', '↙', '↓', '↘']
        step_items = [Button(description=i, layout=button_layout) for i in step_move]

        far_move = ['◤', '▲', '◥', '◄', 'reset', '►', '◣', '▼', '◢']
        far_items = [Button(description=i, layout=button_layout) for i in far_move]

        #'success', 'info', 'warning', 'danger' or ''
        #step_items[4].button_style='info'
        #far_items[4].button_style='info'

        row1 = HBox([step_items[0], step_items[1], step_items[2]])
        row2 = HBox([step_items[3], step_items[4], step_items[5]])
        row3 = HBox([step_items[6], step_items[7], step_items[8]])
        com_a = VBox([row1, row2, row3])

        row4 = HBox([far_items[0], far_items[1], far_items[2]])
        row5 = HBox([far_items[3], far_items[4], far_items[5]])
        row6 = HBox([far_items[6], far_items[7], far_items[8]])
        com_b = VBox([row4, row5, row6])
        
        #step: '↖', '↑', '↗', '←', 'reset', '→', '↙', '↓', '↘'
        step_items[0].on_click(lambda x: self.pt.go_up_left())
        step_items[1].on_click(lambda x: self.pt.go_up())
        step_items[2].on_click(lambda x: self.pt.go_up_right())
        step_items[3].on_click(lambda x: self.pt.go_left())
        step_items[4].on_click(lambda x: self.pt.reset())
        step_items[5].on_click(lambda x: self.pt.go_right())
        step_items[6].on_click(lambda x: self.pt.go_down_left())
        step_items[7].on_click(lambda x: self.pt.go_down() )
        step_items[8].on_click(lambda x: self.pt.go_down_right())

        #far: '◤', '▲', '◥', '◄', 'reset', '►', '◣', '▼', '◢'
        far_items[0].on_click(lambda x: self.pt.upper_left())
        far_items[1].on_click(lambda x: self.pt.far_up())
        far_items[2].on_click(lambda x: self.pt.upper_right())
        far_items[3].on_click(lambda x: self.pt.far_left())
        far_items[4].on_click(lambda x: self.pt.reset())
        far_items[5].on_click(lambda x: self.pt.far_right())
        far_items[6].on_click(lambda x: self.pt.lower_left())
        far_items[7].on_click(lambda x: self.pt.far_down() )
        far_items[8].on_click(lambda x: self.pt.lower_right())
        
        widgets_set1 = HBox([com_a, com_b])
        
        return HBox([com_a, com_b])
        
    def save_snap(self):
        try:
            os.makedirs(self.snap_dir)
        except FileExistsError:
            pass
        localtime = time.strftime("%Y%m%d_%H%M%S", time.localtime())
        image_path = os.path.join(self.snap_dir, localtime + '.jpg')
        with open(image_path, 'wb') as f:
            f.write(self.image_widget.value)
        self.snap_count.value = len(os.listdir(self.snap_dir))
        
    def _read_pos(self):
        self.rl_textbox.value = self.pt.read()[0]
        self.ud_textbox.value = self.pt.read()[1]
        
    def panel_func(self):
        button_layout = widgets.Layout(width='100px', height='80px', align_self='center')

        func_act = ['snapshot', 'save reset', 'position']
        func_items = [Button(description=i, layout=button_layout) for i in func_act]

        func_items[0].button_style='warning'
        func_items[1].button_style='info'
        func_items[2].button_style=''
        
        func_items[0].on_click(lambda x: self.save_snap())
        func_items[1].on_click(lambda x: self.pt.change_reset())
        func_items[2].on_click(lambda x: self._read_pos())
        
        return HBox([func_items[0], func_items[1], func_items[2]])
    
    def snap_box(self):
        return self.snap_count
    
    def play(self):
        slider = self.sliders()
        pos = self.pos_box()
        panel_dir = self.panel_dir()
        panel_func = self.panel_func()
        snap_box = self.snap_box()
        return VBox([HBox([panel_func, slider]), panel_dir, HBox([pos, snap_box])])
    
    def joystick_setup(self, index=0, display=False):
        self.controller = widgets.Controller(index=index)
        display(self.controller) if display==True else print("Now, move your Joystick a bit to activiate...")
        
    def joystick_on(self): # Linking js to pantilt movement control        
        self.controller.buttons[3].observe(lambda x: self._press_act(event="go_up")) # Far Up
        self.controller.buttons[0].observe(lambda x: self._press_act(event="go_down")) # Far Down
        self.controller.buttons[2].observe(lambda x: self._press_act(event="go_left")) # Far Left
        self.controller.buttons[1].observe(lambda x: self._press_act(event="go_right")) # Far Right
        
        self.controller.buttons[9].observe(lambda x: self.pt.reset())
        self.controller.buttons[8].observe(lambda x: self.pt.change_reset())
        self.controller.buttons[17].observe(lambda x: self.save_snap())
        
        self.controller.buttons[6].observe(self._sider_left_cam, names=['value']) # Sliding cam to left
        self.controller.buttons[7].observe(self._sider_right_cam, names=['value']) # Sliding cam to right
        
    def _press_act(self, event):
        self.press_count += 1
        if self.press_count > 7:
            if event == "go_up":
                self.pt.go_up()
            elif event == "go_down":
                self.pt.go_down()
            elif event == "go_left":
                self.pt.go_left()
            elif event == "go_right":
                self.pt.go_right()
            self.press_count = 0

    def joystick_off(self): # Unlinking js to pantilt movement control
        pass
