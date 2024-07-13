from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.card import MDCard
from kivy.uix.screenmanager import ScreenManager, Screen,FadeTransition
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.textfield.textfield import MDTextField
from kivy.animation import Animation
import threading
from kivymd.uix.recyclegridlayout import MDRecycleGridLayout
from kivy.clock import Clock,mainthread
import time
from kivymd.uix.boxlayout import MDBoxLayout ,BoxLayout
from kivy.properties import *
import socket

class Grd(MDGridLayout):
	pass
class Txt1(MDTextField):
	pass
class Spin(MDBoxLayout):
	value=NumericProperty(0)
	def __init__(self, **kwargs):
		super(Spin,self).__init__(**kwargs)
		Clock.schedule_interval(self.spin_fun_start, 0.2/5)
		self.val=0
	def spin_fun_start(self,*args):
		self.val+=1
		self.value=self.val
		if self.val == 100:
			Clock.unschedule(self.spin_fun_start)

      
class S1(Screen):
    pass
class S2(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		#self.ids.dash_spin.active=True
		Clock.schedule_interval(self.add_wget, 0.2/5)
		self.uid1=0
	def add_wget(self, dt):
		self.uid1+=1
		x=Txt1(id=f'trims_{self.uid1}',hint_text='Particular',write_tab=False, max_text_length=9)
		x1=Txt1(id=f'trims_int_{self.uid1}',hint_text='VALUE',write_tab=False, input_filter="float")
		x.opacity=0;x1.opacity=0;self.ids.grd_id.add_widget(x);self.ids.grd_id.add_widget(x1);Animation(opacity=1,duration=.50).start(x);Animation(opacity=1,duration=.50).start(x1)
		if self.uid1 ==39:
			self.remove_widget(self.ids.spin_test)
			self.list_gen()
			Clock.unschedule(self.add_wget)
			self.uid1=0
	def list_gen(self):
		self.l1=[]
		self.l1=[f'trims_int_{i}' for i in range(40)]
		self.ids.dash_spin.active=False
	def id_getfun(self,*args):
		self.ids.grd_id.children[x].text='1'
		#total
		total=0
		data={}
		data1={}
		for val in self.ids.trimes_grid.children:
			if val.id in self.l1:
				if val.text != '':
					total+=float(val.text)
		#add
		for val in self.ids.trimes_grid.children:
			data[val.id]=val.text
		#insert
		for x in self.ids.trimes_grid.children:
			if x.id == data1.key():
				x.text=data1.val()
		#update
		for x in self.ids.trimes_grid.children:
			data1[x.id]=x.text
		#delete
		for x in self.ids.trimes_grid.children:
			x.text=''
	

    

class Test(MDApp):
	def build(self):
		self.sm =ScreenManager()
		#Builder.load_string(KV)
		Builder.load_file("loading.kv")
		self.sm.add_widget(S1(name='s1'))
		self.theme_cls.theme_style = "Light"
		return self.sm
	def on_start(self):
		pass
	def loading_scr(self,scr:str,switch:bool=True):
		if not self.sm.has_screen(scr):
			#self.sm.get_screen('s1').ids.dash_spin_1.active=True
			Builder.load_file("scr1.kv")
			self.sm.add_widget(S2(name='s2'))
		if switch:
			self.sm.current='s2'
			


Test().run()
