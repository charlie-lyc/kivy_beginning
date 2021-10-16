from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager


class MainWindow(Screen):
    pass

class SubWindow(Screen):
    pass

class WindowManager(ScreenManager):
    pass


## No Naming 'mymain.kv'
kv = Builder.load_file('main.kv')


class MyMainApp(App):
    def build(self):
        return kv


if __name__ == '__main__':
    MyMainApp().run()