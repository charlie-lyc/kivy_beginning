## Run to Check Kivy Package Installation
import kivy
################################################################################
from kivy.app import App
from kivy.uix.label import Label


class MyApp(App): # Window Title: 'My' - Except for 'App'
    def build(self):
        return Label(text='Charlie Learns to Code')


################################################################################
if __name__ == '__main__':
    MyApp().run()