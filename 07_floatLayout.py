from kivy.app import App
from kivy.uix.floatlayout import FloatLayout


## Window Title: 'Kivy2'
## Style File: 'kivy2.kv'
class Kivy2App(App):
    def build(self):
        return FloatLayout()


################################################################################
if __name__ == '__main__':
    Kivy2App().run()