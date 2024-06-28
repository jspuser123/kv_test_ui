import threading
from time import sleep
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.clock import Clock
from kivymd.app import MDApp
from kivymd.uix.spinner import MDSpinner
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.scrollview import MDScrollView

KV = '''


MDScreen:

    MDBoxLayout:
        orientation: 'vertical'
        padding: dp(10)
        spacing: dp(10)

        MDSpinner:
            id: spinner
            size_hint: None, None
            size: dp(46), dp(46)
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            active: False

        MDRaisedButton:
            text: "Start Loading"
            pos_hint: {'center_x': 0.5, 'center_y': 0.5}
            on_release: app.start_loading()

        MDScrollView:
            id: scroll
            do_scroll_x: False
            do_scroll_y: True

            MDBoxLayout:
                id: container
                orientation: 'vertical'
                size_hint_y: None
                height: self.minimum_height
                padding: dp(10)
                spacing: dp(10)
'''

class MainScreen(Screen):
    pass

class MyApp(MDApp):

    def build(self):
        return Builder.load_string(KV)

    def start_loading(self):
        # Show the spinner
        self.root.ids.spinner.active = True

        # Create a thread for the loading task
        loading_thread = threading.Thread(target=self.loading_task)
        loading_thread.start()

    def loading_task(self):
        # Simulate a long-running task of loading 100 buttons
        for i in range(100):
            # Sleep to simulate time taken to load each button
            sleep(0.05)
            
            # Schedule adding the button to the main thread
            Clock.schedule_once(lambda dt, i=i: self.add_button(i))

        # Hide the spinner on the main thread
        Clock.schedule_once(lambda dt:self.stop_fun)

    def add_button(self, i):
        self.root.ids.container.add_widget(MDRaisedButton(text=f"Button {i+1}"))
    def stop_fun(self):
        self.root.ids.spinner.active = False

if __name__ == '__main__':
    MyApp().run()
