from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.widget import Widget
from kivy.uix.popup import Popup


class PopupContent(FloatLayout):
    pass


class Widgets(Widget):
    pass


## Window Title: 'Kivy4'
## Style File: 'kivy4.kv'
class Kivy4App(App):
    def build(self):
        self.popup = Popup(
            title='Popup Window',
            content=PopupContent(),
            size_hint=(None, None),
            size=(300, 300)
        )
        return Widgets()


################################################################################
if __name__ == '__main__':
    Kivy4App().run()