###############################################################
## Naming Style File : All Lowercases                        ##
##  ex) Application Name: 'MyApp'   -> Style File: 'my.kv'   ##
##  ex)                   'KivyApp' ->             'kivy.kv' ##
###############################################################

from kivy.app import App
from kivy.uix.widget import Widget


class MyGrid(Widget):
    pass


class KivyApp(App): # Window Title: 'Kivy' - Except for 'App'
    def build(self):
        return MyGrid()


################################################################################
if __name__ == '__main__':
    KivyApp().run()