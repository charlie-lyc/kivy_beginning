from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


class Touch(Widget):
    btn = ObjectProperty()

    ## Using PyCharm
    def on_touch_down(self, touch):
        print('Mouse Down', touch)
        self.btn.opacity = 0.5

    def on_touch_move(self, touch):
        print('Mouse Move', touch)

    def on_touch_up(self, touch):
        print('Mouse Up', touch)
        self.btn.opacity = 1


## Window Title: 'Kivy3'
## Style File: 'kivy3.kv'
class Kivy3App(App):
    def build(self):
        return Touch()


################################################################################
if __name__ == '__main__':
    Kivy3App().run()