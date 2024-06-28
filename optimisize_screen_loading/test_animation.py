from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.properties import NumericProperty
from kivy.graphics import Color, Ellipse
from kivy.uix.widget import Widget
from kivy.animation import Animation
import random

KV = '''

<MyBoxLayout>:
MDScreen:
    MyBoxLayout:

'''

class MyBoxLayout(Widget):
    postion_1_axis=random.randint(10, 600)
    postion_2_axis=random.randint(10, 600)
    postion_3_axis=random.randint(10, 600)
    postion_4_axis=random.randint(10, 600)
    postion_5_axis=random.randint(10, 600)
    # pos_x = NumericProperty(postion_1_axis)
    pos_y = NumericProperty(870)
    def __init__(self, **kwargs):
        super(MyBoxLayout, self).__init__(**kwargs)
        with self.canvas:
            Color(random.randint(0, 9),random.randint(0,9),random.randint(0, 9),0)
            self.l1=Ellipse(size=(40,40),pos=(self.postion_1_axis,self.pos_y))
            Color(random.randint(0, 9),random.randint(0,9),random.randint(0, 9),255)
            self.l2=Ellipse(size=(40,40),pos=(self.postion_2_axis,self.pos_y))
            Color(random.randint(0, 9),random.randint(0,9),random.randint(0, 9),0)
            self.l3=Ellipse(size=(40,40),pos=(self.postion_3_axis,self.pos_y))
            Color(random.randint(0, 9),random.randint(0,9),random.randint(0, 9),0)
            self.l4=Ellipse(size=(40,40),pos=(self.postion_4_axis,self.pos_y))
            Color(random.randint(0, 9),random.randint(0,9),random.randint(0, 9),255)
            self.l5=Ellipse(size=(40,40),pos=(self.postion_5_axis,self.pos_y))
        self.on_closk()
    def on_closk(self,*args):
       Clock.schedule_once(self.rain, 4)

    def rain(self, *args):
        self.pos_y=-100
        self.ani1=Animation(size=(40,40),pos=(self.postion_1_axis,self.pos_y),d=3.).start(self.l1)
        self.ani2=Animation(size=(40,40),pos=(self.postion_2_axis,self.pos_y),d=2.).start(self.l2)
        self.ani3=Animation(size=(40,40),pos=(self.postion_3_axis,self.pos_y),d=3.).start(self.l3)
        self.ani4=Animation(size=(40,40),pos=(self.postion_4_axis,self.pos_y),d=4.).start(self.l4)
        self.ani5=Animation(size=(40,40),pos=(self.postion_5_axis,self.pos_y),d=5.,t='in_quad').start(self.l5)
        Clock.schedule_once(self.clear_fun, 5)

    def clear_fun(self,*args):
        postion_1_y_axis=random.randint(700, 870)
        postion_2_y_axis=random.randint(700, 870)
        postion_3_y_axis=random.randint(700, 870)
        postion_4_y_axis=random.randint(700, 870)
        postion_5_y_axis=random.randint(700, 870)
        self.l1.pos=(self.postion_1_axis,postion_1_y_axis)
        self.l2.pos=(self.postion_2_axis,postion_2_y_axis)
        self.l3.pos=(self.postion_3_axis,postion_3_y_axis)
        self.l4.pos=(self.postion_4_axis,postion_4_y_axis)
        self.l5.pos=(self.postion_5_axis,postion_5_y_axis)
        Clock.schedule_once(self.rain, 4)

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)

    # def on_start(self):
    #     Clock.schedule_interval(self.update, 4)
  

    # def update(self, dt):
    #     print('update')
    #     MyBoxLayout().rain()
Test().run()
