from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.clock import Clock
from kivymd.app import MDApp
from kivy.uix.recycleview import RecycleView
from kivy.uix.recycleboxlayout import RecycleBoxLayout
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.boxlayout import MDBoxLayout

KV = '''
ScreenManager:
    FirstScreen:
    SecondScreen:

<FirstScreen>:
    name: 'first'
    BoxLayout:
        orientation: 'vertical'
        MDRaisedButton:
            text: "Open Second Screen"
            pos_hint: {"center_x": 0.5}
            on_press: app.root.current = 'second'

<SecondScreen>:
    name: 'second'
    BoxLayout:
        id: box_layout
        orientation: 'vertical'
        MDTopAppBar:
            title: "200 MDTextFields"
            pos_hint: {"top": 1}
            left_action_items: [["arrow-left", lambda x: app.go_back()]]
            right_action_items: [["account", lambda args: root.id_get_fun(args)]]
        RecycleView:
            id: rv
            viewclass: 'MDTextField'
            RecycleBoxLayout:
                default_size: None, dp(56)
                default_size_hint: 1, None
                size_hint_y: None
                height: self.minimum_height
                orientation: 'vertical'
              #  disabled: True  # Initially disable the RecycleBoxLayout until data is loaded
    MDCard:
        pos_hint: {'center_x': 0.5,'center_y':.05}
        size_hint:1,.1
        MDRectangleFlatButton:
            text: 'idGet'
            theme_text_color: "Custom"
            text_color: "black"
            line_color: "red"
            on_press:root.id_get_fun(args)
    MDSpinner:
        id: spinner
        size_hint: None, None
        size: dp(46), dp(46)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}
        active: True
'''

class FirstScreen(Screen):
    pass

class SecondScreen(Screen):
    def on_enter(self, *args):
        Clock.schedule_once(self.populate, 0.1)

    def populate(self, dt):
        rv_data = [{'hint_text': f'TextField {i+1}'} for i in range(100)]
        self.ids.rv.data = rv_data
        self.ids.spinner.active=False  # Remove the spinner after loading
    def id_get_fun(self,instance,*args):
        
        # for item in self.ids.rv.data:
        #     widget_id = item['id']
        #     text_field = self.ids.rv.ids.get(widget_id)
        #     if text_field:
        #         print(text_field)
    #    self.ids.rv.data[0] = {'hint_text': f'TextField :2','id': f'T-{0}','text':''} 
    #    print(self.ids.rv.data[1])
        # for child in self.ids.rv.children[0].children:
        #     print(child.id,child.text)
        for child in self.ids.rv.children:
            print(child.children[1].id,child.children[1].text)


class MyApp(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def go_back(self):
        self.root.current = 'first'
   
if __name__ == '__main__':
    MyApp().run()
