import traitlets
import ipywidgets.widgets as widgets
import time
import numpy as np

import bcam
from bcam.utils import bgr8_to_jpeg
from .servo import ServoGroup
import ipywidgets.widgets as widgets
from ipywidgets import Button, HBox, VBox
import os

class PanTilt():
    def __init__(self, rl_ch=12, ud_ch=13, bus=1):
        self.sg = ServoGroup(rl_ch=rl_ch, ud_ch=ud_ch, bus=bus)
        self.sg.reset() #Pan and tilt go to default position
        #Setup various widgets
        self.panel_step_move = NineButton(button_list=['↖', '↑', '↗', '←', 'reset', '→', '↙', '↓', '↘'])
        self.panel_far_move = NineButton(button_list=['◤', '▲', '◥', '◄', 'reset', '►', '◣', '▼', '◢'])
        self.image_widget = widgets.Image(format='jpeg', width=400, height=300) #Display resolution setting
        self.snap_count = widgets.IntText(description='count:', layout=widgets.Layout(width='140px'), value=0)
        self.rl_textbox = widgets.IntText(layout=widgets.Layout(width='140px'), value=self.sg.read()[0], description='rl:')
        self.ud_textbox = widgets.IntText(layout=widgets.Layout(width='140px'), value=self.sg.read()[1], description='ud:')
        self.rl_slider = widgets.FloatSlider(min=-1, max=1, value=0, step=0.02, description='rl')
        self.ud_slider = widgets.FloatSlider(min=-1, max=1, value=0, step=0.02, description='ud')
        self.snap_dir = 'snap' #Folder name for saving snapshot
        self.camera_link = None
        self.controller = None
        self.press_count = 0
        
    def play(self, width_cap=400, height_cap=300, fps=6, flip=0):
        cam = self.cam(width_cap=width_cap, height_cap=height_cap, fps=fps, flip=flip) #Activiate camera and start streaming
        self._setting_step_move() #Buttons widgets for controling step movements
        self._setting_far_move() #Buttons widgets for controling far movements
        slider = self.sliders() #Slider widget for controling movements
        pos = self.pos_box()  #Text widget for showing current position of pan and tilt
        func = self.func() #Function buttons for snapshot, reset default position and update current position
        snap_box = self.snap_box() #Text widget for showing how many pictures in the snapshot folder
        dpA = VBox([self.panel_step_move.display(), self.panel_far_move.display(), func])
        dpB = VBox([slider, pos, snap_box])
        return HBox([cam, dpA, dpB])
        
    def cam(self, cam_type=bcam.JETSON_CAM, width_cap=800, height_cap=600, fps=2, flip=0):
        camera = bcam.config(cam_type=cam_type).resolution(width_cap, height_cap).fps(fps).flip(flip).build()
        camera.start()
        self.camera_link = traitlets.dlink((camera, 'value'), (self.image_widget, 'value'), transform=bgr8_to_jpeg)
        return self.image_widget
    
    def sliders(self):
        self.rl_slider.observe(self._rl_move1, names=['value'])
        self.ud_slider.observe(self._ud_move1, names=['value'])
        return VBox([self.rl_slider, self.ud_slider])
    
    def pos_box(self):
        self.rl_textbox.observe(self._rl_move2, names=['value'])
        self.ud_textbox.observe(self._ud_move2, names=['value'])
        return HBox([self.rl_textbox, self.ud_textbox])
    
    def _read_pos(self):
        self.rl_textbox.value = self.sg.read()[0]
        self.ud_textbox.value = self.sg.read()[1]
    
    def snap_box(self):
        return self.snap_count
        
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
        
    def func(self):
        button_layout = widgets.Layout(width='60px', height='40px', align_self='center')

        func_act = ['snap', 'set', 'pos']
        func_items = [Button(description=i, layout=button_layout) for i in func_act]

        func_items[0].button_style='warning'
        func_items[1].button_style='info'
        func_items[2].button_style=''
        
        func_items[0].on_click(lambda x: self.save_snap())
        func_items[1].on_click(lambda x: self.sg.change_reset())
        func_items[2].on_click(lambda x: self._read_pos())
        
        return HBox([func_items[0], func_items[1], func_items[2]])
    
    def controller_setup(self, index=0, dp=False):
        self.controller = widgets.Controller(index=index)
        print("Move your controller NOW and activiate it...")
        display(self.controller)
        
    def controller_on(self): # Linking js to pantilt movement control        
        self.controller.buttons[3].observe(lambda x: self._press_act(event="go_up")) # Far Up
        self.controller.buttons[0].observe(lambda x: self._press_act(event="go_down")) # Far Down
        self.controller.buttons[2].observe(lambda x: self._press_act(event="go_left")) # Far Left
        self.controller.buttons[1].observe(lambda x: self._press_act(event="go_right")) # Far Right
        
        self.controller.buttons[9].observe(lambda x: self.sg.reset())
        self.controller.buttons[8].observe(lambda x: self.sg.change_reset())
        self.controller.buttons[17].observe(lambda x: self.save_snap())
        
        self.controller.buttons[6].observe(self._sider_left_cam, names=['value']) # Sliding cam to left
        self.controller.buttons[7].observe(self._sider_right_cam, names=['value']) # Sliding cam to right
    
    def _setting_step_move(self):
        #step: '↖', '↑', '↗', '←', 'reset', '→', '↙', '↓', '↘'
        self.panel_step_move.buttons[0].on_click(lambda x: self.sg.go_up_left())
        self.panel_step_move.buttons[1].on_click(lambda x: self.sg.go_up())
        self.panel_step_move.buttons[2].on_click(lambda x: self.sg.go_up_right())
        self.panel_step_move.buttons[3].on_click(lambda x: self.sg.go_left())
        self.panel_step_move.buttons[4].on_click(lambda x: self.sg.reset())
        self.panel_step_move.buttons[5].on_click(lambda x: self.sg.go_right())
        self.panel_step_move.buttons[6].on_click(lambda x: self.sg.go_down_left())
        self.panel_step_move.buttons[7].on_click(lambda x: self.sg.go_down() )
        self.panel_step_move.buttons[8].on_click(lambda x: self.sg.go_down_right())
    
    def _setting_far_move(self):
        #far: '◤', '▲', '◥', '◄', 'reset', '►', '◣', '▼', '◢'
        self.panel_far_move.buttons[0].on_click(lambda x: self.sg.upper_left())
        self.panel_far_move.buttons[1].on_click(lambda x: self.sg.far_up())
        self.panel_far_move.buttons[2].on_click(lambda x: self.sg.upper_right())
        self.panel_far_move.buttons[3].on_click(lambda x: self.sg.far_left())
        self.panel_far_move.buttons[4].on_click(lambda x: self.sg.reset())
        self.panel_far_move.buttons[5].on_click(lambda x: self.sg.far_right())
        self.panel_far_move.buttons[6].on_click(lambda x: self.sg.lower_left())
        self.panel_far_move.buttons[7].on_click(lambda x: self.sg.far_down() )
        self.panel_far_move.buttons[8].on_click(lambda x: self.sg.lower_right())
        
    def _rl_val(self, val):
        return int((val * (self.sg.rl.upper - self.sg.rl.lower) + self.sg.rl.upper + self.sg.rl.lower) / 2)
    
    def _ud_val(self, val):
        return int((val * (self.sg.rl.upper - self.sg.rl.lower) + self.sg.rl.upper + self.sg.rl.lower) / 2)

    def _rl_move1(self, change):
        val = change['new']
        self.sg.to_angle(rl=self._rl_val(val=val))

    def _ud_move1(self, change):
        val = change['new']
        self.sg.to_angle(ud=self._ud_val(val=val))
        
    def _rl_move2(self, change):
        val = change['new']
        self.sg.to_angle(rl=val)
        
    def _ud_move2(self, change):
        val = change['new']
        self.sg.to_angle(ud=val)
        
    def _sider_to_left(self, val):
        return self.sg.rl.upper * val - (val - 1) * (self.sg.rl.upper - self.sg.rl.lower) / 2
    
    def _sider_to_right(self, val):
        return self.sg.rl.lower * val - (val - 1) * (self.sg.rl.upper - self.sg.rl.lower) / 2
    
    def _sider_left_cam(self, change):
        val = change['new']
        if self.controller.buttons[7].value == 0:
            self.sg.to_angle(rl=self._sider_to_left(val=val))

    def _sider_right_cam(self, change):
        val = change['new']
        if self.controller.buttons[6].value == 0:
            self.sg.to_angle(rl=self._sider_to_right(val=val))
            
    def _press_act(self, event):
        self.press_count += 1
        if self.press_count > 7:
            if event == "go_up":
                self.sg.go_up()
            elif event == "go_down":
                self.sg.go_down()
            elif event == "go_left":
                self.sg.go_left()
            elif event == "go_right":
                self.sg.go_right()
            self.press_count = 0
    
class NineButton():
    def __init__(self, button_list=None):
        self.button_layout = widgets.Layout(width='60px', height='40px', align_self='center')
        self.button_list = ['Fwd', '▲', 'sL', '◄', 'Stop', '►', 'Bwd', '▼', 'sR'] if button_list==None else button_list
        self.buttons = [Button(description=i, layout=self.button_layout) for i in self.button_list]
        
    def display(self):
        row1 = HBox([self.buttons[0], self.buttons[1], self.buttons[2]])
        row2 = HBox([self.buttons[3], self.buttons[4], self.buttons[5]])
        row3 = HBox([self.buttons[6], self.buttons[7], self.buttons[8]])
        return VBox([row1, row2, row3])
