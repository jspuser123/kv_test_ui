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

class Grd(MDGridLayout):
	pass
class Txt1(MDTextField):
	pass
class S1(Screen):
    pass
class S2(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.ids.dash_spin.active=True
		threading.Thread(target=self.fun_start).start()
		threading.Thread(target=self.th_fun).start()
	def th_fun(self,*args):
		for incre in range(200):
			time.sleep(0.1/2)
			self.ids.persentage.text=f'{incre}%'
		self.ids.persentage.text=''
	#@mainthread0
	def fun_start(self,*args):
		for uid in range(200):
			time.sleep(0.1/2) 
			Clock.schedule_once(lambda dt, uid=uid: self.add_wget(uid))
		self.ids.dash_spin.active=False
	def add_wget(self, uid):
		x=Txt1(id=f'textid{uid}',hint_text=f'textid{uid}');x.opacity=0;self.ids.grd_id.add_widget(x);Animation(opacity=1,duration=.50).start(x)
	def id_getfun(self,*args):
		# self.ids.grd_id.children[2].text
		for co , x in enumerate(self.ids.grd_id.children):
			if co == 2: 
				print(x.id,x.text)
				

    

class Test(MDApp):
	def build(self):
		self.sm =ScreenManager()
		#Builder.load_string(KV)
		Builder.load_file("loading.kv")
		self.sm.add_widget(S1(name='s1'))
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

# __dir__()
# ['prop', 'obj', 'last_op', '__module__', '__init__', '__setitem__', '__delitem__', '__setslice__', '__delslice__', '__iadd__', '__imul__', 'append',
#   'remove', 'insert', 'pop', 'extend', 'sort', 'reverse', '__dict__', '__weakref__', '__doc__', '__new__', '__repr__', '__hash__', '__getattribute__',
#     '__lt__', '__le__', '__eq__', '__ne__', '__gt__', '__ge__', '__iter__', '__len__', '__getitem__', '__add__', '__mul__', '__rmul__', '__contains__', '__reversed__',
# 	  '__sizeof__', 'clear', 'copy', 'index', 'count',
#   '__class_getitem__', '__str__', '__setattr__', '__delattr__', '__reduce_ex__', '__reduce__', '__subclasshook__', '__init_subclass__', '__format__', '__dir__', '__class__']